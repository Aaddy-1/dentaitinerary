from fastapi import APIRouter
from data.models.payload_models import DentistMatchPayload
from src.services.dentist_matching import dentist_matcher

router = APIRouter(prefix="/match", tags=["AI"])


# @router.get("/users/", tags=["users"])
# async def read_users():
#     return [{"username": "Rick"}, {"username": "Morty"}]


# @router.get("/users/me", tags=["users"])
# async def read_user_me():
#     return {"username": "fakecurrentuser"}


# @router.get("/users/{username}", tags=["users"])
# async def read_user(username: str):
#     return {"username": username}


@router.post("/dentist", tags=["dentist"])
async def match_user_to_dentist(item: DentistMatchPayload):
    dental_preferences = item.dental_preferences
    cosine_similarity = await dentist_matcher(dental_preferences)
    return cosine_similarity
