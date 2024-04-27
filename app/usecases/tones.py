from typing import Annotated, Optional, List, Tuple
from app.repositories.tones import ToneRepository

from app.model.tones.tone_model import Tones
from app.model.languages.languages_model import Languages

from fastapi import Depends

class ToneUsecase:
    toneRepository: ToneRepository

    def __init__(
            self,
            toneRepository: Annotated[ToneRepository, Depends()]
    ) -> None:
        self.toneRepository = toneRepository
    
    def list_by_language_id(self, language_id: int) -> List[Tones]:
        return self.toneRepository.list_by_language_id(language_id)

    def get_by_id(self, id: int) -> Optional[Tones]:
        return self.toneRepository.get_by_id(id)