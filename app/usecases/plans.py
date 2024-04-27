from typing import Annotated, Optional
from app.repositories.plans import PlanRepository

from app.model.plans.plans_model import Plans

from fastapi import Depends

class PlanUsecases: 
    planRepository : PlanRepository

    def __init__(
            self,
            planRepostiory: Annotated[PlanRepository, Depends()]
    ) -> None:
        self.planRepository = planRepostiory

    def get_by_id(self, id: int) -> Optional[Plans]:
        return self.planRepository.get_by_id(id)
    
    def get_by_plan_type(self, plan_type: str) -> Optional[Plans]:
        return self.planRepository.get_by_plan_type(plan_type)
    
    def get_by_product_id(self, product_id: str) -> Optional[Plans]:
        return self.planRepository.get_by_product_id(product_id)
    