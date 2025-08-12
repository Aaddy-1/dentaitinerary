from pydantic import BaseModel, Field, model_validator
from typing_extensions import Self


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
    cost_max: float

    @model_validator(mode="after")
    def validate_costs(self) -> Self:
        if self.cost_max < self.cost_min:
            raise ValueError("Passwords do not match")
        return self
