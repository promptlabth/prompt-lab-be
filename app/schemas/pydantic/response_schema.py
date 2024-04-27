from pydantic import BaseModel
from pydantic.generics import GenericModel
from typing import Generic, TypeVar

T = TypeVar("T")
class ResponseSchema(GenericModel, Generic[T]):
    status_code: int
    data: T