from beanie import Document
from typing import List
from models.common_models import Address
from pydantic import Field, EmailStr


class DentalClinic(Document):
    # A model containing information about a dental clinic
    clinic_id: str
    name: str
    dentists: List[str] = []  # A list containing dentist IDs
    address: Address
    rating: float = Field(..., ge=0.0, le=5.0)
    email: EmailStr

    class Settings:
        name = "clinics"
