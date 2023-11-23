# Make migrations with tortoise-orm (aerich)
## Install packages
```
pip install fastapi uvicorn[standard] tortoise-orm[asyncpg] aerich
```
## Create ORM config in `_db.py`
```
POSTGRES_DB = "db"
POSTGRES_USER = "user"
POSTGRES_PASSWORD = "password"
POSTGRES_HOST = "localhost"
POSTGRES_PORT = "5432"

TORTOISE_ORM = {
    "connections": {"default": f'postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'},
    "apps": {
        "user": {
            "models": [
                "repositories.db.models.user", "aerich.models"
            ],
            "default_connection": "default",
        },
    },
}
```
## When you at projects root directory (Tortoise-ORM) use this to create .toml file
```
> aerich init -t config._db.TORTOISE_ORM --location repositories/db/migrations
```
And then
```
> aerich init-db
```

## Apply migrations (if db aldready initialized):
```
> aerich migrate
> aerich upgrade
```