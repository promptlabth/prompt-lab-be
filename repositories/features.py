from typing import List, Annotated
from sqlmodel import Session, select, col

from fastapi import Depends

from model.database import get_session
from model.features.features_model import Features

class FeatureRepository:

    session: Session

    def __init__(
            self,
            session : Annotated[Session, Depends(get_session)]
    ) -> None:
        self.session = session

    def list(self) -> List[Features]:
        statement = select(Features).order_by(col(Features.id).asc())
        result = self.session.exec(statement)
        return result.first()
    
    def get_by_id(self, id : int) -> Features | None:
        statement = select(Features).where(Features.id == id)
        result = self.session.exec(statement)
        return result.first()
