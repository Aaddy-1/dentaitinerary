from beanie import Document
from pydantic import Field, model_validator
from typing import List, Dict
from datetime import date
from typing_extensions import Self
from uuid import UUID, uuid4

from data.models.common_models import SpecialtyCost


class Dentist(Document):
    # Model to represent a single dentist
    dentist_id: UUID = Field(default_factory=uuid4)
    clinic_id: UUID
    first_name: str
    last_name: str
    specialties: List[str]
    years_of_experience: int = Field(..., ge=0)
    languages_spoken: List[str]
    rating: float = Field(..., ge=0.0, le=5.0)
    cost: Dict[str, SpecialtyCost]
    availability: List[date]

    @model_validator(mode="after")
    def validate_specialty_costs(self) -> Self:
        """
        Validates that every specialty in the cost dictionary
            is also in the specialties list.
        """
        cost_specialties = set(self.cost.keys())
        listed_specialties = set(self.specialties)

        if not cost_specialties.issubset(listed_specialties):
            mismatched_specialties = cost_specialties - listed_specialties
            raise ValueError(
                f"Specialties in cost do not match the specialties list: {mismatched_specialties}"
            )
        return self

    class Settings:
        name = "dentists"
