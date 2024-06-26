from typing import Annotated, List, Optional
from sqlmodel import Session, select, col

from fastapi import Depends

from app.model.database import get_session
from app.model.models.models_model import Models

class ModelRepository:
    session: Session
    
    def __init__(
            self,
            session: Annotated[Session, Depends(get_session)]
    ) -> None:
        self.session = session
        return None
    
    def list(self) -> List[Models]:
        statment = select(Models).order_by(col(Models.id).asc())
        result = self.session.exec(statment)
        return result.all()
    
    def get_by_id(self, id: int) -> Optional[Models]:
        statement = select(Models).where(Models.id == id)
        result = self.session.exec(statement)
        return result.first()
    
    def get_by_name(self, name: str) -> Optional[Models]:
        statement = select(Models).where(Models.model_name == name)
        result = self.session.exec(statement)
        return result.first()