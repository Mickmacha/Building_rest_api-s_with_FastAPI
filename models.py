from pydantic import BaseModel
from uuid import uuid4, UUID
from typing import Optional, List
from enum import Enum


class Gender(str, Enum):
    male = "male"
    female = "female"


class Role(str, Enum):
    admin = "admin"
    student = "Student"
    moderator = "Moderator"


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    name: str
    email: str
    gender: Gender
    role: List[Role]
