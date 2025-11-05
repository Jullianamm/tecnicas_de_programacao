from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

# Conexão com o banco de dados SQLite
DATABASE_URL = "sqlite:///system_users.db"
engine = create_engine(DATABASE_URL)

# Base para criar os modelos
Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Integer()