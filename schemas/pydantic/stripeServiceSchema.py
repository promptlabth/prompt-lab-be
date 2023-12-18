from pydantic import BaseModel

from datetime import datetime

class StartEndPlan(BaseModel):
    start_date: datetime
    end_date: datetime