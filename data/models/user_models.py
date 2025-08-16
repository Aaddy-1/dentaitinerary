from beanie import Document
from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import Field


class User(Document):
    # A model to represent the user's profile and needs.
    id: UUID = Field(default_factory=uuid4)
    email: str
    password_hash: str  # Storing the hash, not the raw password
    dental_needs: List[str]
    preferences: dict  # e.g., {"budget": 3000, "travel_style": "relaxed"}
    anonymized_health_data: Optional[str] = None  # Hashed or encrypted PHI
    interests: List[str]  # e.g., ["history", "yoga", "adventure"]
    travel_dates: Optional[dict] = None

    class Settings:
        name = "users"
