from sqlalchemy import Column, Integer, String, Boolean
from datos.db import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, nullable=False)
