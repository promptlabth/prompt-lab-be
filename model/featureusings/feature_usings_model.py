from typing import Optional, TYPE_CHECKING
from sqlmodel import Field, Session, SQLModel, create_engine, Relationship
from datetime import date,time

if TYPE_CHECKING:
    from model.users.users_model import Users
    from model.features.features_model import Features
class Featureusings(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    dates: date
    timestart:time
    timestop:time

    # Relationship

    # 1 featureusings have 1 user
    user_id: Optional[int] = Field(default=None, foreign_key="users.id")
    user: Optional["Users"] = Relationship(back_populates="featureusings")

    # 1 featureusing have 1 feature
    feature_id: Optional[int] = Field(default=None, foreign_key="features.id")
    feature: Optional["Features"] = Relationship(back_populates="featureusings")
