from datetime import datetime
from typing import List, Tuple
from models.appointment import AppointmentModel
from models.employee import UserModel
from models.patient import PatientModel

class AppointmentRepository:
    ''' Manage all queries about Appointments '''
    def __init__(self, db):
        self.db = db
        self.now = datetime.now()

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
        description=None
    ):
        appointment = AppointmentModel(
            appointment_date=appointment_date,
            patient_id=patient_id,
            doctor_id=doctor_id,
            patient_attended=patient_attended,
            drug_allergy=drug_allergy,
            description=description,
            modified_in=str(self.now)
        )
        self.db.session.add(appointment)
        self.db.session.commit()

    def update_appointment_info(self, appointment_id, patient_id, date, doctor_id):
        query = self.db.session\
            .query(AppointmentModel)\
            .filter(
                AppointmentModel.id == str(appointment_id)
            ).update({
                "patient_id": str(patient_id),
                "appointment_date": str(date),
                "patient_attended": False,
                "doctor_id": str(doctor_id),
                "modified_in": str(self.now)
            })
        self.db.session.commit()

    def find_appointment_id(self, appointment_id):
        query = self.db.session\
            .query(AppointmentModel.id)\
            .filter(
                AppointmentModel.id == str(appointment_id)
            ).first()
        return query
