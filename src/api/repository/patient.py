from models.patient import PatientModel
#from config.database import DBConnection

class PatientRepository:
    ''' Manage all queries about patients and his appointments '''
    def __init__(self, db):
        self.db = db

    def find_patient(self, info):
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
