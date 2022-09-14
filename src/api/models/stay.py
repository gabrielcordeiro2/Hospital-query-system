from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy import ForeignKey, Enum
from config.database import Base
import enum

class StatusType(enum.Enum):
    discharged = "discharged"
    observation = "observation"
    admitted = "admitted"

class StayModel(Base):
    __tablename__ = 'stay'

    id = Column(Integer, primary_key=True)
    stay_date = Column(DateTime)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    doctor_id = Column(Integer, ForeignKey('employees.id'))
    drug_allergy = Column(String(30))
    description = Column(Text)
    status = Column(Enum(StatusType))
    room = Column(String(3))
    bed = Column(String(2))
    modified_in = Column(DateTime)
