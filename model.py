from typing import TypeVar, Optional, Generic
from pydantic import BaseModel

T = TypeVar('T')


class Book(BaseModel):
    id: Optional[str] = None
    title: str
    description: str


class Response(BaseModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T] = None
