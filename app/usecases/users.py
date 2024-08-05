
from typing import List, Annotated, Optional
from app.repositories.users import UsersRepository
from app.repositories.plans import PlanRepository

from fastapi import Depends

from app.model.users.users_model import Users

from app.schemas.pydantic.userSchema import UserUpdateRequest

class UsersUsecase:
    usersRepository: UsersRepository
    plan_repository: PlanRepository
    

    def __init__(
            self,
            userRepository: Annotated[UsersRepository, Depends()],
            plan_repository: Annotated[PlanRepository, Depends()]
    ) -> None:
        self.usersRepository = userRepository
        self.plan_repository = plan_repository

    def list(
            self
    ) -> List[Users]:
        return self.usersRepository.list()
    
    def get(
            self,
            id: int
    ) -> Optional[Users] :
        return self.usersRepository.get(id)
    
    def get_by_firebase_id(
            self,
            firebase_id: str
    ) -> Optional[Users]:
        return self.usersRepository.get_by_firebase_id(firebase_id)
    
    def get_by_stripe_id(
            self,
            stripe_id: str
    ) -> Optional[Users]:
        return self.usersRepository.get_by_stripe_id(stripe_id)
    
    def create(
            self,
            user: Users
    ) -> Users:
        return self.usersRepository.create(user)

    def update(
            self,
            id: int,
            user: UserUpdateRequest
    ) -> Users:
        return self.usersRepository.update(id, user)
    
    def get_max_message_of_user(
            self,
            firebase_id :str,
    ) -> Optional[int]:
        user = self.usersRepository.get_by_firebase_id(firebase_id)
        if user == None:
            return None
        plan = self.plan_repository.get_by_id(user.plan_id)
        if plan == None:
            return None
        return plan.max_messages