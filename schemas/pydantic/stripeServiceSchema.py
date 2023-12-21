from typing import Optional

from pydantic import BaseModel

from datetime import datetime

class StartEndPlan(BaseModel):
    start_date: Optional[datetime]
    end_date: Optional[datetime]