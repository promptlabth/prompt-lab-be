from typing import Annotated
from repositories.tones import ToneRepository

from model.tones.tone_model import Tones

from fastapi import Depends

class ToneUsecase:
    toneRepository: ToneRepository

    def __init__(
            self,
            toneRepository: Annotated[ToneRepository, Depends()]
    ) -> None:
        self.toneRepository = toneRepository

    def get_by_id(self, id: int) -> Tones | None:
        return self.toneRepository.get_by_id(id)