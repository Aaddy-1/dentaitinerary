from pydantic import BaseModel, Field, EmailStr
from typing import List

from common_models import Address
from dentist_models import Dentist


class DentalClinic(BaseModel):
    # A model containing information about a dental clinic
    clinic_id: str
    name: str
    dentists: List[Dentist] = []
    address: Address
    rating: float = Field(..., ge=0.0, le=5.0)
    email: EmailStr
