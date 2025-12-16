import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv # Importar dotenv

load_dotenv() # Cargar las variables del archivo .env

# Antes: DATABASE_URL = "sqlite:///app.db"
# Ahora: Leemos desde el entorno, con un valor por defecto por seguridad
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///app.db")

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)

