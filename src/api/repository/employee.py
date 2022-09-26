from models.employee import UserModel

class EmployeeRepository:
    ''' Manage all queries about employees '''
    def __init__(self, db):
        self.db = db

    def find_doctor_id(self, info: str):
        doctor = self.db.session\
            .query(UserModel.id)\
            .filter(
                UserModel.name == str(info),
                UserModel.type == 'doctor'
            ).first()
        return doctor
