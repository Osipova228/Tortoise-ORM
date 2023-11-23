from fastapi import FastAPI
from tortoise import Tortoise
from repositories.db.base import BaseRepository
from repositories.db.models import RolesEnum
from repositories.db.users import UserRepository

app = FastAPI()

tortoise_instance = Tortoise()
base_repo = BaseRepository(tortoise_instance)
user_repo = UserRepository(tortoise_instance)


async def init():
    await base_repo.init()
    await user_repo.init()


async def shutdown():
    await base_repo.close()
    await user_repo.close()

# Пример создания пользователя (взаимодействие с бд)
async def create_user():
    await user_repo.add_user("test", "test", RolesEnum.VOLUNTEER)


@app.on_event("startup")
async def startup_event():
    await init()


@app.on_event("shutdown")
async def shutdown_event():
    await shutdown()


@app.get("/create_user")
async def create_user_endpoint():
    await create_user()
    return {"message": "Пользователь создан"}


# Запуск приложения
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
