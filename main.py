from fastapi import FastAPI
from tortoise import Tortoise
from repositories.db.base import BaseRepository
from repositories.db.users import UserRepository

app = FastAPI()

tortoise_instance = Tortoise()
base_repo = BaseRepository(tortoise_instance)
user_repo = UserRepository(tortoise_instance)


# Запуск приложения
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)