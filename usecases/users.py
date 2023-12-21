
from typing import List, Annotated, Optional
from repositories.users import UsersRepository

from fastapi import Depends

from model.users.users_model import Users

from schemas.pydantic.userSchema import UserUpdateRequest

class UsersUsecase:
    usersRepository: UsersRepository

    def __init__(
            self,
            userRepository: Annotated[UsersRepository, Depends()]
    ) -> None:
        self.usersRepository = userRepository

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