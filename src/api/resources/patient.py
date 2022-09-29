from typing import Dict, List
from flask_restful import Resource, reqparse
from globals import importResource
from repository.patient import PatientRepository

conn = importResource('conn', 'config.database_instance')

def resource_arguments():
    arguments = reqparse.RequestParser()
    arguments.add_argument('name', type=str, required=True, help="The field 'name' cannot be left blank.")
    arguments.add_argument('cpf')
    arguments.add_argument('birthdate')
    arguments.add_argument('phone')
    arguments.add_argument('sus_card')
    return arguments

class Patient(Resource):
    ''' Find or Update Patients info endpoint methods '''
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        print('Patient was instantiated')
        self.repo = PatientRepository(conn)
        self.arguments = resource_arguments()

    def get(self, info: str) -> List:
        response = self.repo.find_patient(info)
        result = []

        for patient in response:
            json_patient = {
                'name': patient.name,
                'birthdate': str(patient.birthdate),
                'cpf': patient.cpf,
                'phone': patient.phone,
                'sus_card': patient.sus_card
            }
            result.append(json_patient)

        if result:
            return result
        return {'message': 'User not found'}, 404

    def put(self, info: str) -> Dict:
        data = self.arguments.parse_args()
        patient_found = self.repo.find_patient(info)

        if patient_found and patient_found[0].name != info:
            self.repo.update_patient_info(info, **data)
            return {'message': 'Patient updated successfully!'}, 200
        return {"message": f"Oops, '{info}' patient info not found."}, 404

class PatientRegister(Resource):
    ''' Create Patient endpoint method '''
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        print('Patient was instantiated')
        self.repo = PatientRepository(conn)
        self.arguments = resource_arguments()

    def post(self) -> Dict:
        data = self.arguments.parse_args()
        cpf_found = self.repo.find_patient(data.get('cpf'))
        sus_card_found = self.repo.find_patient(data.get('sus_card'))

        if cpf_found:
            return {
                "message": f"Patient with cpf '{data.get('cpf')}' already exists."
            }, 400

        if sus_card_found:
            return {
                "message": f"Patient with sus_card '{data.get('sus_card')}' already exists."
            }, 400

        self.repo.register_patient(**data)
        return {'message': 'Patient created successfully!'}, 201
