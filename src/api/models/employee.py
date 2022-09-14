from sqlalchemy import Column, Integer, String
from sqlalchemy import Enum
from config.database import Base
import enum

class UserType(enum.Enum):
    atendente = "attendant"
    enf_geral = "head_nurse"
    medico = "doctor"

class UserModel(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    user = Column(String(10), nullable=False, unique=True)
    password = Column(String(20), nullable=False)
    type = Column(Enum(UserType), nullable=False)
