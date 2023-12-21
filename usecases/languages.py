from typing import Annotated, Optional

from model.languages.languages_model import Languages

from fastapi import Depends

from repositories.languages import LanguageRepository


class LanguageUsecase:

    languageRepository: LanguageRepository
    def __init__(
            self,
            languageRepository: Annotated[LanguageRepository, Depends()]
    ) -> None:
        self.languageRepository = languageRepository

    def get_by_id(self, id:int) -> Optional[Languages]:
        return self.languageRepository.get_by_id(id)
    