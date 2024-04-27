from typing import Annotated, Optional

from fastapi import Depends

from app.repositories.features import FeatureRepository
from app.model.features.features_model import Features

class FeatureUsecase:
    featureRepository: FeatureRepository

    def __init__(
            self,
            featureRepository: Annotated[FeatureRepository, Depends()]
    ) -> None:
        self.featureRepository = featureRepository

    def get_by_id(self, id: int) -> Optional[Features]:
        return self.featureRepository.get_by_id(id)
    
    