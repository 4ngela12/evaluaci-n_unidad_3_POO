import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = "Sistema de Gestión de TODOs"
VERSION = "1.0"

API_BASE_URL = "https://jsonplaceholder.typicode.com"

SECRET_KEY = os.getenv("SECRET_KEY")

if SECRET_KEY is None:
    raise Exception("SECRET_KEY no encontrada en .env")

