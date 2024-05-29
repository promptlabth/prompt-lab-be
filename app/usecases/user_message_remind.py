from typing import List, Annotated, Optional
from fastapi import Depends
from app.repositories.user_message_remind import UserMessageRemindRepository


from app.model.user_balance_messages.user_balance_messages_model import UserMessageBalance

class UserMessageRemindUsecase:
    userMessageRemindRepository: UserMessageRemindRepository

    def __init__(
            self, 
            userMessageRemindRepo: Annotated[UserMessageRemindRepository, Depends()]
    )-> None:
        self.userMessageRemindRepository = userMessageRemindRepo

    def getUserRemind(self, firebase_id: str) -> Optional[UserMessageBalance]:
        return self.userMessageRemindRepository.getUserRemind(firebase_id)
    
    def upsertUserRemind(self, user_remind: UserMessageBalance) -> UserMessageBalance:
        return self.userMessageRemindRepository.upsertUserRemind(user_remind)
    
    def updateUserRemind(self, user_remind: UserMessageBalance) -> UserMessageBalance:
        return self.userMessageRemindRepository.updateUserRemind(user_remind)