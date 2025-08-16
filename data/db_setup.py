import os
import asyncio
from dotenv import load_dotenv
from pymongo import AsyncMongoClient
from beanie import init_beanie
from data.models.clinic_models import DentalClinic
from data.models.dentist_models import Dentist
from data.models.user_models import User
from data.models.itinerary_models import Itinerary


async def init_db():
    load_dotenv()
    # Create Motor client
    connection_url = os.getenv("MONGODB_URL")

    if not connection_url:
        raise ValueError("MONGODB_CONNECTION_URL environment variable not set.")

    database_name = os.getenv("DATABASE_NAME")

    client = AsyncMongoClient(connection_url)

    # Initialize beanie with all top-level documents
    await init_beanie(
        database=client[database_name],
        document_models=[DentalClinic, Dentist, User, Itinerary],
    )


async def main():
    await init_db()
    print("Database successfully initialized!")


if __name__ == "__main__":
    asyncio.run(main())
