from typing import Annotated

from repositories.prompt_messages import PromptMessageRepository

from fastapi import Depends

from model.promptMessages.prompt_messages_model import Promptmessages

class PromptMessageUsecase:
    promptMessageRepository: PromptMessageRepository

    def __init__(
            self,
            promptMessageRepository: Annotated[
                PromptMessageRepository, Depends()
            ]
    ) -> None:
        self.promptMessageRepository = promptMessageRepository
        return None
    
    def create(self, promptMessage: Promptmessages) -> Promptmessages:
        return self.promptMessageRepository.create(
            promptMessage=promptMessage
        )
    
    def get_count_this_month_by_user_id(
            self,
            user_id: int
    ) -> int:
        return self.promptMessageRepository.get_count_this_month_by_user_id(
            user_id
        )