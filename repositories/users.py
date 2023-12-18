from sqlmodel import Session, select, col

from model.database import get_session
from model.users.users_model import Users

from typing import List, Optional

from fastapi import Depends

from schemas.pydantic.userSchema import UserUpdateRequest

from pydantic import BaseModel



class UsersRepository:
    session : Session

    def __init__(self, session:Session = Depends(get_session)) -> None:
        self.session = session

    def list(self) -> List[Users]:
        statement = select(Users).order_by(col(Users.id).asc())
        result = self.session.exec(statement=statement)
        return result.all()
    
    def get_by_firebase_id(self, firebase_id: str) -> Users | None:
        statement = select(Users).where(Users.firebase_id == firebase_id)
        result = self.session.exec(statement=statement)
        return result.first()
    
    def get_by_stripe_id(self, stripe_id: str) -> Users | None:
        statement = select(Users).where(Users.stripe_id == stripe_id)
        result = self.session.exec(statement=statement)
        return result.first()

    def get(self, id: int) -> Users | None:
        statement = select(Users).where(Users.id == id)
        result = self.session.exec(statement=statement)
        return result.first()
    
    def create(self, user: Users) -> Users:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    
    def update(self, id:int, user: UserUpdateRequest) -> Users | None:
        db_user = self.session.get(Users, id)
        if not db_user:
            return None
        for key, value in user:
            setattr(db_user, key, value)
        db_user.id = id
        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)
        return db_user

    def delete(self, id: int) -> int: 
        user = self.get(id)
        id = user.id
        self.session.delete(user)
        return id
    