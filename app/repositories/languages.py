from typing import List, Annotated, Optional
from sqlmodel import Session, select, col

from fastapi import Depends

from app.model.database import get_session
from app.model.languages.languages_model import Languages

class LanguageRepository:
    session : Session

    def __init__(
            self,
            session: Annotated[Session, Depends(get_session)]
    ) -> None:
        self.session = session
    
    def list(self) -> List[Languages]:
        statement = select(Languages).order_by(col(Languages.id).asc())
        result = self.session.exec(statement)
        return result.all()
    
    def get_by_language(self, language: str) -> Optional[Languages]:
        statement = select(Languages).where(Languages.language_name == language)
        result = self.session.exec(statement)
        return result.first()
    
    def get_by_id(self, id: int) -> Optional[Languages]:
        statement = select(Languages).where(Languages.id == id)
        result = self.session.exec(statement)
        return result.first()