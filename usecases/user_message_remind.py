from typing import List, Annotated, Optional
from fastapi import Depends
from repositories.user_message_remind import UserMessageRemindRepository


from model.user_message_reminds.user_message_reminds_model import UserMessageReminds

class UserMessageRemindUsecase:
    userMessageRemindRepository: UserMessageRemindRepository

    def __init__(
            self, 
            userMessageRemindRepo: Annotated[UserMessageRemindRepository, Depends()]
    )-> None:
        self.userMessageRemindRepository = userMessageRemindRepo

    def getUserRemind(self, firebase_id: str) -> Optional[UserMessageReminds]:
        return self.userMessageRemindRepository.getUserRemind(firebase_id)
    
    def upsertUserRemind(self, user_remind: UserMessageReminds) -> UserMessageReminds:
        return self.userMessageRemindRepository.upsertUserRemind(user_remind)
    
    def updateUserRemind(self, user_remind: UserMessageReminds) -> UserMessageReminds:
        return self.userMessageRemindRepository.updateUserRemind(user_remind)