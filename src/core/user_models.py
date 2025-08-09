from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date


class User(BaseModel):
    # A model to represent the user's profile and needs.
    anonymized_id: str  # A hashed ID for privacy
    email: str
    password_hash: str  # Storing the hash, not the raw password


class UserProfile(BaseModel):
    # Detailed user profile for AI matching
    user_id: str  # Foreign key linking to the main User model
    dental_needs: List[str]
    preferences: dict  # e.g., {"budget": 3000, "travel_style": "relaxed"}
    anonymized_health_data: Optional[str] = None  # Hashed or encrypted PHI
    interests: List[str]  # e.g., ["history", "yoga", "adventure"]
    travel_dates: Optional[dict] = None
