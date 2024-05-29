from typing import  Annotated, Optional
from sqlmodel import Session, select
from fastapi import Depends

from app.model.database import get_session
from app.model.user_balance_messages.user_balance_messages_model import UserMessageBalance

class UserBalanceMessageRepository:
    session: Session
    def __init__(
            self, 
            session: Annotated[Session, Depends(get_session)]
    ) -> None: 
        self.session = session
    
    def getUserBalance(self, firebase_id: str) -> Optional[UserMessageBalance]:
        statement = select(UserMessageBalance).where(
            UserMessageBalance.firebase_id == firebase_id
        )
        result = self.session.exec(statement)
        return result.first()

    def upsertUserBalance(self, userBalance: UserMessageBalance) -> UserMessageBalance: 
        self.session.add(userBalance)
        self.session.commit()
        self.session.refresh(userBalance)
        return userBalance

    def updateUserBalance(self, user_remind: UserMessageBalance) -> UserMessageBalance:
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
        