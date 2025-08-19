# main.py

from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.utils.tfidf_utils import tfidf_utils
from data.db_setup import init_db
from data.models.dentist_models import Dentist
import src.routers.matching_router as matching_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Handles application startup and shutdown events.
    """
    print("Application starting up...")
    await init_db()
    print("Database connection established!")

    app.state.tfidf_dentist = tfidf_utils()

    all_dentists = await Dentist.find_all().to_list()

    if all_dentists:
        dentist_specialties = [" ".join(d.specialties) for d in all_dentists]
        dentist_ids = [str(d.dentist_id) for d in all_dentists]
        app.state.tfidf_dentist.fit_vectorizer(dentist_specialties, dentist_ids)
    else:
        print("No Dentists found, vectorizer not fitted.")

    yield
    print("Application shutting down...")


app = FastAPI(lifespan=lifespan)
app.include_router(matching_router.router)


@app.get("/")
async def root():
    """
    A simple root endpoint to confirm the app is running.
    """
    return {"message": "DentAItinerary AI Module is running!"}
