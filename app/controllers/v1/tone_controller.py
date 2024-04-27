from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException

from app.model.tones.tone_model import Tones

from app.usecases.tones import ToneUsecase
from app.usecases.languages import LanguageUsecase

from app.schemas.pydantic.toneSchema import ToneResponse, LanguageResponse


tone_routers = APIRouter(
    tags=["Tone Model service", "v1"],
    prefix="/v1/tone",
    responses={
        404:{"description" : "Tone Error or Not Found"}
    }
)


@tone_routers.get("/{language}", status_code=200, response_model=List[ToneResponse])
def get_by_language(
    language : str,
    toneUsecase: Annotated[ToneUsecase, Depends()],
    languageUsecase: Annotated[LanguageUsecase, Depends()]
) -> List[ToneResponse]:
    db_language = languageUsecase.get_by_language(language)
    if(db_language is None):
        raise HTTPException(status_code=404, detail="not found a language")

    db_tone = toneUsecase.list_by_language_id(db_language.id)
    result : List[ToneResponse] = []
    for tone in db_tone:
        result.append(
            ToneResponse(
                id=tone.id,
                tone_name=tone.tone_name,
                language_id=tone.language_id,
                language=LanguageResponse(
                    id=db_language.id,
                    language_name=db_language.language_name
                )
            )
        )

    return result

@tone_routers.get("/{id}", status_code=200, response_model=Tones)
def get_by_id(
    id: int,
    toneUsecase : Annotated[ToneUsecase, Depends()]
) -> Tones:
    db_tone = toneUsecase.get_by_id(id)
    if db_tone is None:
        raise HTTPException(status_code=404, detail="not found a language")
    return db_tone