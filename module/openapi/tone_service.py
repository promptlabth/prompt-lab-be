"""
module for API tones
"""

from fastapi import APIRouter,  HTTPException
from pydantic import BaseModel
from sqlmodel import select

from model import database

from model.tones import tone_model
from model.languages import languages_model

router = APIRouter(
    tags=["Tone Service For add data"],
    responses={
        404:{
            "discription": "Not found"
        }
    }
)

class Language(BaseModel):
    id:int
    language_name:str

class Tone(BaseModel):
    id:int
    tone_name:str
    language_id:int
    language:Language


    

@router.get("/tones/{language}", status_code=200, response_model=list[Tone])
def list_tones(language) -> list[Tone]:
    tones = []
    with database.session_engine() as session:
        
        # # find language by id
        # try:
        #     statement = select(languages_model.Languages).where(languages_model.Languages.language_name == language)
        #     result = session.exec(statement=statement)
        #     lang = result.one()
        # except:
        #     raise HTTPException(status_code=404, detail="Not found languages")
        
        # find all tones
        try:
            statement = select(tone_model.Tones).where(tone_model.Tones.language.language_name == language)
            result = session.exec(statement)
            tones_exec = result.all()
        except:
            raise HTTPException(status_code=404, detail="Not found tones")
        
        # append all tone and lang to list

        try:
            for tone_exec in tones_exec:
                tone = Tone(
                    id=tone_exec.id,
                    tone_name=tone_exec.tone_name,
                    language_id=lang.id,
                    language=Language(
                    id=lang.id,
                    language_name=lang.language_name
                    )
                )
                tones.append(tone)
        except:
            raise HTTPException(status_code=401, detail="Can't create Tone model")

    return tones


@router.get("/tone/{id}", status_code=200, response_model=Tone)
def get_tone_by_id(id) -> Tone:
    tone = Tone
    with database.session_engine() as session:
        
        try:
            statement = select(tone_model.Tones).where(tone_model.Tones.id == id)
            result = session.exec(statement=statement)
            tone_exec = result.one()
        except:
            raise HTTPException(status_code=404, detail="Not found tones")
        
        try:
            statement = select(languages_model.Languages).where(languages_model.Languages.id == tone_exec.language_id)
            result = session.exec(statement=statement)
            lang_exec = result.one() 
        except:
            raise HTTPException(status_code=404, detail="Not found language")

        

        try:
            tone = Tone(
            id=id, 
            tone_name=tone_exec.tone_name, 
            language_id=tone_exec.language_id,
            language= Language(
                id=lang_exec.id,
                language_name=lang_exec.language_name
                )
            )
        except:
            raise HTTPException(status_code=401, detail="cannot create a tone")
    
    return tone



