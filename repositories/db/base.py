from tortoise import Tortoise

from config import POSTGRES_DB, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_USER


class BaseRepository:

    def __init__(self, tortoise_instance: Tortoise):
        self.tortoise_instance = tortoise_instance

    async def init(self):
        await self.tortoise_instance.init(
            db_url=f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}',
            modules={'models': ['internal.repositories.db.models']}
        )
        await self.tortoise_instance.generate_schemas()

    async def close(self):
        await self.tortoise_instance.close_connections()
