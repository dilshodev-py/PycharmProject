import asyncio
from dataclasses import dataclass

from pydantic.v1 import BaseModel
from pydantic.v1 import validator

from bot.enums import RoleEnum, LangEnum
from db.config import CRUD

class UserJob(CRUD, BaseModel):
    id: int = None
    user_id: int = None
    job_id: int = None



class User(CRUD, BaseModel):
    id: int = None
    first_name: str = None
    last_name: str = None
    phone_number: str = None
    language: str = LangEnum.en.name
    description: str = None
    role: str = RoleEnum.user.name

    @classmethod
    @validator('phone_number')
    async def phone_number_validator(cls, phone_number):
        if phone_number.startswith("+"):
            return phone_number[1:]
        return phone_number

    @classmethod
    @validator('role')
    async def role_validator(cls, role):
        if role in RoleEnum.value:
            return RoleEnum(role).name

    @property
    async def fullname(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Category(CRUD, BaseModel):
    id: int = None
    name: str = None

class Job(CRUD, BaseModel):
    id: int = None
    name: str = None
    category_id : int = None

    async def filter_by_category(self):
        jobs:list[Job] = await self.objects
        result = []
        for job in jobs:
            if job.category_id == self.category_id:
                result.append(job)
        return result

