from sqlalchemy import Column, Integer, String
from datos.db import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    # Agregamos (100) o (50) para limitar el tamaño
    nombre = Column(String(100), nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(255), nullable=False)
