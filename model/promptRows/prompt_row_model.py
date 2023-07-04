from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from model.promptMessages.prompt_messages_model import Promptmessages

# Why we should need it?
# can Optimize this database to best practice ?
# Or we need to link a 2 record in 1 table ?
# TODO What is good?
class Promptrows(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    row_number: int

    # 1 promptrows have 1 prev prompt
    prev_prompt_id : Optional[int] = Field(default=None, foreign_key="promptmessages.id")
    prev_prompt: Optional["Promptmessages"] = Relationship(back_populates="promptrows")