from pydantic import BaseModel

from datetime import datetime

class StartEndPlan(BaseModel):
    start_date: datetime | None
    end_date: datetime | None