from sqlmodel import Session, select, col

from model.database import get_session
from model.plans.plans_model import Plans
from fastapi import Depends

class PlanRepository:
    session: Session

    def __init__(
            self,
            session: Session = Depends(get_session)
    ) -> None:
        self.session = session

    def get_by_id(self, id: int) -> Plans | None:
        statement = select(Plans).where(Plans.id == id)
        result = self.session.exec(statement=statement)
        return result.first()
    
    def get_by_plan_type(self, plan_type: str) -> Plans | None:
        statement = select(Plans).where(Plans.planType == plan_type)
        result = self.session.exec(statement)
        return result.first()
    
    def get_by_product_id(self, product_id: str) -> Plans | None:
        statement = select(Plans).where(Plans.product_id == product_id)
        result = self.session.exec(statement)
        return result.first()