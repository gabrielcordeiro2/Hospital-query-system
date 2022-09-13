from sqlalchemy import Column, Integer, String, Date
from config.database import Base

class PacienteModel(Base):
    __tablename__ = 'pacientes'

    id = Column(Integer, primary_key=True)
    nome = Column(String(60))
    cpf = Column(String(12))
    nascimento = Column(Date)
    telefone = Column(String(12))
    cartao_sus = Column(String(18))

