import os

DATABASE_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "ferreira@))1"),
    "database": os.getenv("DB_NAME", "imoveis_db"),
}