from typing import Annotated

from sqlmodel import Session, select, and_
from fastapi import Depends

from model.database import get_session
from model.inputPrompts.input_prompt_model import InputPrompts


class InputPromptRepository:
    session: Session

    def __init__(
            self,
            session: Annotated[Session, Depends(get_session)]
    ) -> None:
        self.session = session
        return None
    
    def get_by_id(self, id: int) -> InputPrompts | None:
        statement = select(InputPrompts).where(InputPrompts.id == id)
        result = self.session.exec(statement).first()
        return result.first()
    
    def get_by_feature_id_and_model_id(self, feature_id: int, model_id: int, language_id: int) -> InputPrompts | None:
        statement = select(InputPrompts).where(
            and_(
                InputPrompts.feature_id == feature_id,
                InputPrompts.model_id == model_id ,
                InputPrompts.language_id == language_id
                )
        )
        result = self.session.exec(statement)
        return result.first()