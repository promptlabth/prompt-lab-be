import logging
from typing import List, Annotated, Optional
from sqlmodel import Session, select, col

from fastapi import Depends

from app.model.database import get_session
from app.model.users.users_model import Users

class FacebookRepository:

    session: Session

    def __init__(
            self,
            session : Annotated[Session, Depends(get_session)]
    ) -> None:
        self.session = session

    def get_facebook_token_by_user_id(self, id: str) -> Optional[str]:
        try:
            statement = select(Users).where(Users.firebase_id == id)
            result = self.session.exec(statement)
            result = result.first()
            logging.info(result)
            if result.platform != 'facebook':
                return None
            return result.access_token
        except Exception as e:
                logging.error(e)
                return None