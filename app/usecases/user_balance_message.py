from typing import List, Annotated, Optional
from fastapi import Depends
from app.repositories.user_balance_message import UserBalanceMessageRepository


from app.model.user_balance_messages.user_balance_messages_model import UserMessageBalance

class UserBalanceMessageUsecase:
    userBalanceMessageRepository: UserBalanceMessageRepository

    def __init__(
            self, 
            userBalanceMessageRepo: Annotated[UserBalanceMessageRepository, Depends()]
    )-> None:
        self.userBalanceMessageRepository = userBalanceMessageRepo

    def getUserBalance(self, firebase_id: str) -> Optional[UserMessageBalance]:
        return self.userBalanceMessageRepository.getUserBalance(firebase_id)
    
    def upsertUserBalance(self, user_remind: UserMessageBalance) -> UserMessageBalance:
        return self.userBalanceMessageRepository.upsertUserBalance(user_remind)
    
    def updateUserBalance(self, user_remind: UserMessageBalance) -> UserMessageBalance:
        return self.userBalanceMessageRepository.updateUserBalance(user_remind)