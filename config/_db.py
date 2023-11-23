POSTGRES_DB = "postgres"
POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "admin"
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
