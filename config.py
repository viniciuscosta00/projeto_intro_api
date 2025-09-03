import os
from urllib.parse import quote_plus

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY', 'wcc@2023")
    password = os.getenv("DATABASE_PASSWORD", "wcc@2023")
    enconded_password = quote_plus(password)
    SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", f"postgresql://postgres:{enconded_password}@127.0.0.1:5432/tarefas3A")


    #SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL" , "postgresql://postgres:SECRET_KEY@127.0.0.1:5432/tarefas3A")
    SQLALCHEMY_TRACK_MODIFICATIONS = False