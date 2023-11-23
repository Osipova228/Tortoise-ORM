from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator
from aiobcrypt import hashpw, checkpw, gensalt
from enum import Enum


class RolesEnum(Enum):
    ADMIN = 'admin'
    VOLUNTEER = 'volunteer'


class User(Model):
    login = fields.CharField(max_length=255, pk=True)
    password = fields.CharField(max_length=255, null=False)
    role = fields.CharEnumField(RolesEnum, default=RolesEnum.VOLUNTEER)

    class Meta:
        table = 'users'


User_Pydantic = pydantic_model_creator(User, name='User')


async def hash_password(password: str) -> str:
    salt = await gensalt()

    hashed_password = await hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')


async def check_password(password: str, hashed_password: str) -> bool:
    return await checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
