from typing import List, Tuple
from config.database import DBConnection
from models.appointment import AppointmentModel
from models.employee import UserModel
from models.patient import PatientModel

class PatientRepository:
    ''' Manage all queries about patients and his appointments '''

    def __init__(self, db):
        self.db = db

    def find_patient(self, info: str) -> List[Tuple]:
        patient_query = self.db.session\
            .query(PatientModel)\
            .filter(
                (PatientModel.name == str(info)) |
                (PatientModel.cpf == str(info)) |
                (PatientModel.sus_card == str(info))
            ).with_entities(
                PatientModel.name,
                PatientModel.birthdate,
                PatientModel.cpf,
                PatientModel.phone,
                PatientModel.sus_card
            ).all()
        return patient_query

    def register_patient(self, name, cpf, birthdate, phone, sus_card):
        with DBConnection() as db:
            register_info = PatientModel(
                name=name,
                cpf=cpf, 
                birthdate=birthdate,
                phone=phone,
                sus_card=sus_card)
            db.session.add(register_info)
            db.session.commit()

    def update_patient_info(self, info, name=None, cpf=None, birthdate=None, phone=None, sus_card=None):
        ''' Update Patient info searching by "cpf" or "sus_card" '''
        patient_query = self.db.session\
            .query(PatientModel)\
            .filter(
                (PatientModel.cpf == str(info)) |
                (PatientModel.sus_card == str(info))
            ).update({
                'name': name,
                'cpf': cpf, 
                'birthdate': birthdate,
                'phone': phone,
                'sus_card': sus_card
            })
        self.db.session.commit()

    def find_appointments(self, info: str) -> List[Tuple]:
        appointment_query = self.db.session\
            .query(AppointmentModel)\
            .join(PatientModel,
                PatientModel.id == AppointmentModel.patient_id)\
            .join(UserModel,
                UserModel.id == AppointmentModel.doctor_id)\
            .filter(
                (PatientModel.name == str(info)) |
                (PatientModel.cpf == str(info)) |
                (PatientModel.sus_card == str(info))
            ).with_entities(
                PatientModel.name.label('patient_name'),
                AppointmentModel.appointment_date,
                AppointmentModel.patient_attended,
                UserModel.name.label('doctor_name')
            ).all()
        return appointment_query
