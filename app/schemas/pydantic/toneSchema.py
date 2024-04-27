from pydantic import BaseModel


class LanguageResponse(BaseModel):
    id:int
    language_name:str

class ToneResponse(BaseModel):
    id:int
    tone_name:str
    language_id:int
    language:LanguageResponse