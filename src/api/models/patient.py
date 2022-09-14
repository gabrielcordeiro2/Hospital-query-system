from sqlalchemy import Column, Integer, String, Date
from config.database import Base

class PatientModel(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True)
    name = Column(String(60))
    cpf = Column(String(12))
    birthdate = Column(Date)
    phone = Column(String(12))
    sus_card = Column(String(18))

