from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy import ForeignKey
from config.database import Base

class ConsultaModel(Base):
    __tablename__ = 'consultas'

    id = Column(Integer, primary_key=True)
    data_consulta = Column(DateTime)
    paciente_id = Column(Integer, ForeignKey('pacientes.id'), nullable=False)
    medico_id = Column(Integer, ForeignKey('funcionarios.id'))
    paciente_compareceu = Column(Boolean)
    alergia_medicamento = Column(String(30))
    descricao = Column(Text)
    modificado_em = Column(DateTime)
