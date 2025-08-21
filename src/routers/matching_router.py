from fastapi import APIRouter, Depends
from data.models.payload_models import DentistMatchPayload
from src.services.dentist_matching import dentist_matcher
from src.utils.tfidf_utils import tfidf_utils
from src.dependencies import get_dentist_tfidf

router = APIRouter(prefix="/match", tags=["AI"])


@router.post("/dentist", tags=["dentist"])
async def match_user_to_dentist(
    item: DentistMatchPayload,
    dentist_instance: tfidf_utils = Depends(get_dentist_tfidf),
):
    dental_preferences = item.dental_preferences
    cosine_similarity = await dentist_matcher(dental_preferences, dentist_instance)
    return cosine_similarity
