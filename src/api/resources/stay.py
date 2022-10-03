from typing import Dict, List
from flask_restful import Resource, reqparse
from globals import importResource
from repository.employee import EmployeeRepository
from repository.patient import PatientRepository
from repository.stay import StayRepository

conn = importResource('conn', 'config.database_instance')

def resource_arguments():
    arguments = reqparse.RequestParser()
    #arguments.add_argument('stay_id')
    arguments.add_argument('stay_date')
    arguments.add_argument('patient_info')
    arguments.add_argument('doctor_name')
    arguments.add_argument('status')
    arguments.add_argument('room')
    arguments.add_argument('bed')
    return arguments

class Stay(Resource):
    ''' Find Stay info endpoint methods '''
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        print('Stay was instantiated')
        self.repo = StayRepository(conn)
        self.repo2 = PatientRepository(conn)
        self.arguments = resource_arguments()

    def get(self, info):
        patient_found = self.repo2.find_patient_id(info)

        if patient_found:
            response = self.repo.find_stay(patient_found.id)
            result = []

            for stay in response:
                json_patient = {
                    'stay_id': stay.stay_id,
                    'stay_date': str(stay.stay_date),
                    'patient_name': stay.patient_name,
                    'doctor_name': stay.doctor_name,
                    'status': stay.status.value,
                    'room': stay.room,
                    'bed': stay.bed
                }
                result.append(json_patient)

            if result:
                return result
            return {'message': 'Stay not found'}, 404
        return {'message': 'Patient not found'}, 404

class StayRegister(Resource):
    ''' Register Stay endpoint method '''
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        print('Stay was instantiated')
        self.repo = PatientRepository(conn)
        self.repo2 = EmployeeRepository(conn)
        self.repo3 = StayRepository(conn)
        self.arguments = resource_arguments()

    def post(self):
        data = self.arguments.parse_args()
        patient_found = self.repo.find_patient_id(data.get('patient_info'))
        doctor_found = self.repo2.find_doctor_id(data.get('doctor_name'))

        if patient_found and doctor_found:
            result = self.repo3.register_stay(
                stay_date=data.get('stay_date'),
                patient_id=patient_found.id,
                doctor_id=doctor_found.id,
                status=data.get('status'),
                room=data.get('room'),
                bed=data.get('bed')
            )
            return {'message': 'Appointment successfully registered!'}, 201
        return {'message': 'Error, patient or doctor information not found.'}, 404

class StayUpdate(Resource):
    ''' Update Stay endpoint method '''
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        print('Stay was instantiated')
        self.repo = StayRepository(conn)
        self.repo2 = PatientRepository(conn)
        self.repo3 = EmployeeRepository(conn)
        self.arguments = resource_arguments()

    def put(self, stay_id):
        data = self.arguments.parse_args()
        patient_found = self.repo2.find_patient_id(data.get('patient_info'))
        doctor_found = self.repo3.find_doctor_id(data.get('doctor_name'))

        if patient_found and doctor_found:
            stay_found = self.repo.find_stay_id(stay_id)
            if stay_found:
                print(data.get('stay_date'))
                self.repo.update_stay_info(
                    stay_id=stay_found.id,
                    stay_date=data.get('stay_date'),
                    patient_id=patient_found.id,
                    doctor_id=doctor_found.id,
                    status=data.get('status'),
                    room=data.get('room'),
                    bed=data.get('bed')
                )
                return {'message': 'Patient successfully updated!'}
            return {'message': 'Error, Stay not found'}, 404
        return {'message': 'Error, patient or doctor information not found.'}, 404