from pydantic import BaseModel
from typing import List


class DentistMatchPayload(BaseModel):
    dental_preferences: List[str]
    budget: float
    consent: bool
