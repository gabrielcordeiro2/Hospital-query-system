from typing import List, Tuple
from models.patient import PatientModel

class PatientRepository:
    ''' Manage all queries about patients '''
    def __init__(self, db):
        self.db = db

    def find_patient(self, info: str) -> List[Tuple]:
        ''' Find Patients info searching by "name", "cpf" or "sus_card" '''
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
        ''' Find Patient_id searching by "name", "cpf" or "sus_card" '''
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
                sus_card=sus_card
            )
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
