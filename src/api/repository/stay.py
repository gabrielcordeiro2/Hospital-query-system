from datetime import datetime
from models.employee import UserModel
from models.patient import PatientModel
from models.stay import StayModel

class StayRepository:
    ''' Manage all queries about stay '''
    def __init__(self, db):
        self.db = db
        self.now = datetime.now()

    def find_stay(self, patient_id):
        query = self.db.session\
            .query(StayModel)\
            .join(PatientModel,
                PatientModel.id == StayModel.patient_id)\
            .join(UserModel,
                UserModel.id == StayModel.doctor_id)\
            .filter(
                StayModel.patient_id == patient_id
            ).with_entities(
                StayModel.id.label('stay_id'),
                StayModel.stay_date,
                PatientModel.name.label('patient_name'),
                UserModel.name.label('doctor_name'),
                StayModel.status,
                StayModel.room,
                StayModel.bed
            ).all()
        return query

    def register_stay(
        self,
        stay_date,
        patient_id,
        doctor_id,
        status,
        room,
        bed
    ):
        stay = StayModel(
            stay_date=stay_date,
            patient_id=patient_id,
            doctor_id=doctor_id,
            status=status,
            room=room,
            bed=bed,
            modified_in=str(self.now)
        )
        self.db.session.add(stay)
        self.db.session.commit()

    def update_stay_info(
        self,
        stay_id,
        stay_date,
        patient_id,
        doctor_id,
        status,
        room,
        bed
    ):
        self.db.session\
            .query(StayModel)\
            .filter(StayModel.id == stay_id)\
            .update({
                'stay_date': str(stay_date),
                'patient_id': patient_id,
                'doctor_id': doctor_id,
                'status': status,
                'room': room,
                'bed': bed,
                'modified_in': str(self.now)
            })
        self.db.session.commit()

    def find_stay_id(self, stay_id):
        query = self.db.session\
            .query(StayModel.id)\
            .filter(StayModel.id == str(stay_id))\
            .first()
        return query
