from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
from datetime import date

from common_models import SpecialtyCost


class Dentist(BaseModel):
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
