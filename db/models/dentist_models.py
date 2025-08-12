from beanie import Document
from pydantic import Field
from typing import List
from datetime import date

from models.common_models import SpecialtyCost


class Dentist(Document):
    # Model to represent a single dentist
    dentist_id: str
    clinic_id: str  # Foreign key linking to the DentalClinic model
    first_name: str
    last_name: str
    specialties: List[str]  # e.g., ["implants", "root canal", "cosmetic"]
    years_of_experience: int = Field(..., ge=0)
    languages_spoken: List[str]
    rating: float = Field(..., ge=0.0, le=5.0)
    cost: SpecialtyCost  # Use the existing SpecialtyCost model
    availability: List[date]

    class Settings:
        name = "dentists"
