from typing import Annotated, Optional

from repositories.model import ModelRepository

from fastapi import Depends

from model.models.models_model import Models

class ModelUsecase:
    modelRepository: ModelRepository

    def __init__(
            self,
            modelRepository: Annotated[ModelRepository, Depends()]
    ) -> None:
        self.modelRepository = modelRepository
        return None
    
    def get_by_name(self, name:str) -> Optional[Models]:
        return self.modelRepository.get_by_name(name)