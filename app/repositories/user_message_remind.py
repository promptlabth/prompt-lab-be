from typing import  Annotated, Optional
from sqlmodel import Session, select
from fastapi import Depends

from app.model.database import get_session
from app.model.user_message_reminds.user_message_reminds_model import UserMessageReminds

class UserMessageRemindRepository:
    session: Session
    def __init__(
            self, 
            session: Annotated[Session, Depends(get_session)]
    ) -> None: 
        self.session = session
    
    def getUserRemind(self, firebase_id: str) -> Optional[UserMessageReminds]:
        statement = select(UserMessageReminds).where(
            UserMessageReminds.firebase_id == firebase_id
        )
        result = self.session.exec(statement)
        return result.first()

    def upsertUserRemind(self, userRemind: UserMessageReminds) -> UserMessageReminds: 
        self.session.add(userRemind)
        self.session.commit()
        self.session.refresh(userRemind)
        return userRemind

    def updateUserRemind(self, user_remind: UserMessageReminds) -> UserMessageReminds:
        statement = select(UserMessageReminds).where(
            UserMessageReminds.firebase_id == db_user_remind.firebase_id
            )
        result = self.session.exec(statement)
        db_user_remind = result.first()

        for key, value in user_remind:
            setattr(db_user_remind, key, value)
        db_user_remind.firebase_id = db_user_remind.firebase_id

        self.session.add(db_user_remind)
        self.session.commit()
        self.session.refresh(db_user_remind)
        return db_user_remind
        