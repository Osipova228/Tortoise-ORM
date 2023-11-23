from tortoise import Tortoise

from repositories.db.models import RolesEnum, User
from repositories.db.base import BaseRepository
from repositories.db.models.user import hash_password


class UserRepository(BaseRepository):
    def __init__(self, tortoise_instance: Tortoise):
        super().__init__(tortoise_instance)

    async def get_user(self, login: str) -> User:
        try:
            return await User.get(login=login)
        except User.DoesNotExist:
            return None

    async def get_user_role(self, login: str):
        user = await self.get_user(login)
        return user.role.value if user else None

    async def get_all_users(self):
        return await User.all()

    async def add_user(self, login: str, password: str, role: RolesEnum):
        hashed_password = await hash_password(password)
        await User.create(login=login, password=hashed_password, role=role.value)

    async def update_user(self, login: str, password: str = None, role: RolesEnum = None):
        user = await self.get_user(login)

        if user:
            if password:
                user.password = await hash_password(password)

            if role:
                user.role = role.value

            await user.save()

    async def delete_user(self, login: str):
        user = await self.get_user(login)
        if user:
            await user.delete()
