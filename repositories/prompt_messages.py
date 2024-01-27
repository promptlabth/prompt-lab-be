from typing import List, Annotated

from sqlmodel import Session

from fastapi import Depends

from model.database import get_session
from model.promptMessages.prompt_messages_model import Promptmessages

from datetime import datetime
from sqlmodel import Session, select, col
from sqlalchemy import func, and_

class PromptMessageRepository:
    session: Session

    def __init__(
            self,
            session: Annotated[Session, Depends(get_session)]
    ) -> None:
        self.session = session
    
    def create(self, promptMessage:Promptmessages) -> Promptmessages:
        self.session.add(promptMessage)
        self.session.commit()
        self.session.refresh(promptMessage)
        return promptMessage
    
    def get_count_this_month_by_user_id(
            self,
            user_id: int
    ) -> int:
            # Get the current year and month
            current_year = datetime.utcnow().year
            current_month = datetime.utcnow().month

            # Modify the query to count messages for the current month
            statement_prompt = select([func.count()]).where(
                and_(
                    Promptmessages.user_id == user_id,
                    func.extract('year', Promptmessages.date_time) == current_year,
                    func.extract('month', Promptmessages.date_time) == current_month
                )
            )

            # Execute the query and get the count
            total_messages_this_month = self.session.execute(statement_prompt).scalar()
            if total_messages_this_month is None:
                return 0
            return total_messages_this_month