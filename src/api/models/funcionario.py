from sqlalchemy import Column, Integer, String
from sqlalchemy import Enum
from config.database import Base
import enum

class UserType(enum.Enum):
    atendente = "atendente"
    enf_geral = "enf_geral"
    medico = "medico"

class UserModel(Base):
    __tablename__ = 'funcionarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    usuario = Column(String(10), nullable=False, unique=True)
    senha = Column(String(20), nullable=False)
    tipo = Column(Enum(UserType), nullable=False)
