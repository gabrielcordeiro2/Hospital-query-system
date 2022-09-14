from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy import ForeignKey
from config.database import Base

class AppointmentModel(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True)
    appointment_date = Column(DateTime)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    doctor_id = Column(Integer, ForeignKey('employees.id'))
    patient_attended = Column(Boolean)
    drug_allergy = Column(String(30))
    description = Column(Text)
    modified_in = Column(DateTime)
