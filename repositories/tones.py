from typing import List, Annotated, Optional, Tuple
from sqlalchemy import and_
from sqlmodel import Session, select, col
from fastapi import Depends


from model.tones.tone_model import Tones
from model.database import get_session
from model.languages.languages_model import Languages


class ToneRepository:
    session :Session

    def __init__(
            self,
            session: Annotated[Session, Depends(get_session)]
    ) -> None:
        self.session = session

    def list(self) -> List[Tones]:
        statement = select(Tones).order_by(col(Tones.id).asc())
        result = self.session.exec(statement)
        return result.all()

    def list_by_language_id(self, language_id: int) -> List[Tones]:
        statement = select(Tones).where( 
                Tones.language_id == language_id
            )
        result = self.session.exec(statement)
        return result.all()

    def get_by_id(self, id: int) -> Optional[Tones]:
        statement = select(Tones).where(Tones.id == id)
        result = self.session.exec(statement)
        return result.first()
    