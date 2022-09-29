from datetime import datetime
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

    def find_patient_id(self, info: str):
        patient_query = self.db.session\
            .query(PatientModel.id)\
            .filter(
                (PatientModel.name == str(info)) |
                (PatientModel.cpf == str(info)) |
                (PatientModel.sus_card == str(info))
            ).first()
        return patient_query

    def register_patient(self, name, cpf, birthdate, phone, sus_card):
            register_info = PatientModel(
                name=name,
                cpf=cpf, 
                birthdate=birthdate,
                phone=phone,
                sus_card=sus_card)
            self.db.session.add(register_info)
            self.db.session.commit()

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
                AppointmentModel.id,
                PatientModel.name.label('patient_name'),
                AppointmentModel.appointment_date,
                AppointmentModel.patient_attended,
                UserModel.name.label('doctor_name')
            ).all()
        return appointment_query

    def schedule_appointment(
        self,
        appointment_date,
        patient_id,
        doctor_id,
        patient_attended=None,
        drug_allergy=None,
        description=None):

        now = datetime.now()

        appointment = AppointmentModel(
            appointment_date=appointment_date,
            patient_id=patient_id,
            doctor_id=doctor_id,
            patient_attended=patient_attended,
            drug_allergy=drug_allergy,
            description=description,
            modified_in=str(now))
        self.db.session.add(appointment)
        self.db.session.commit()

    def update_appointment_info(self, appointment_id, patient_id, date, doctor_id):
        with DBConnection() as db:
            query = db.session\
                .query(AppointmentModel)\
                .filter(
                    AppointmentModel.id == str(appointment_id)
                ).update({
                    "patient_id": str(patient_id),
                    "appointment_date": str(date),
                    "patient_attended": False,
                    "doctor_id": str(doctor_id)
                })
            db.session.commit()

    def find_appointment_id(self, appointment_id):
        with DBConnection() as db:
            query = db.session\
                .query(AppointmentModel.id)\
                .filter(
                    AppointmentModel.id == str(appointment_id)
                ).first()
            return query