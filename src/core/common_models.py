from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date


class Address(BaseModel):
    # A model containing information about an address
    street: str
    city: str
    state: str
    pincode: str
    country: str = "India"


class SpecialtyCost(BaseModel):
    # Cost of a specialty
    specialty: str
    cost_min: float = Field(..., gt=0)
    cost_max: float = Field(..., gt=cost_min)
