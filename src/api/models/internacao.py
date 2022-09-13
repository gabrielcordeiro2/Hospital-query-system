from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy import ForeignKey, Enum
from config.database import Base
import enum

class StatusType(enum.Enum):
    alta = "alta"
    observacao = "observacao"
    internado = "internado"

class InternacaoModel(Base):
    __tablename__ = 'internacoes'

    id = Column(Integer, primary_key=True)
    data_internacao = Column(DateTime)
    paciente_id = Column(Integer, ForeignKey('pacientes.id'))
    medico_id = Column(Integer, ForeignKey('funcionarios.id'))
    alergia_medicamento = Column(String(30))
    descricao = Column(Text)
    status = Column(Enum(StatusType))
    quarto = Column(String(3))
    leito = Column(String(2))
    modificado_em = Column(DateTime)
