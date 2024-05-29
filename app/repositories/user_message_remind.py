from typing import  Annotated, Optional
from sqlmodel import Session, select
from fastapi import Depends

from app.model.database import get_session
from app.model.user_balance_messages.user_balance_messages_model import UserMessageBalance

class UserMessageRemindRepository:
    session: Session
    def __init__(
            self, 
            session: Annotated[Session, Depends(get_session)]
    ) -> None: 
        self.session = session
    
    def getUserRemind(self, firebase_id: str) -> Optional[UserMessageBalance]:
        statement = select(UserMessageBalance).where(
            UserMessageBalance.firebase_id == firebase_id
        )
        result = self.session.exec(statement)
        return result.first()

    def upsertUserRemind(self, userRemind: UserMessageBalance) -> UserMessageBalance: 
        self.session.add(userRemind)
        self.session.commit()
        self.session.refresh(userRemind)
        return userRemind

    def updateUserRemind(self, user_remind: UserMessageBalance) -> UserMessageBalance:
        statement = select(UserMessageBalance).where(
            UserMessageBalance.firebase_id == db_user_remind.firebase_id
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
        