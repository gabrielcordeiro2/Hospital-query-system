from flask import jsonify
from flask_restful import Resource
from globals import importResource
from repository.patient import PatientRepository

from flask_restful import reqparse

conn = importResource('conn', 'config.database_instance')

class Patient(Resource):
    ''' Find or Update Patients info endpoint methods '''
    arguments = reqparse.RequestParser()
    arguments.add_argument('name', type=str, required=True, help="The field 'name' cannot be left blank.")
    arguments.add_argument('cpf')
    arguments.add_argument('birthdate')
    arguments.add_argument('phone')
    arguments.add_argument('sus_card')

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        print('Patient was instantiated')
        self.repo = PatientRepository(conn)

    def get(self, info: str):
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

    def put(self, info):
        data = self.arguments.parse_args()
        patient_found = self.repo.find_patient(info)
        print(patient_found)

        if patient_found:
            self.repo.update_patient_info(info, **data)
            return {'message': 'Patient updated successfully!'}, 200
        return {"message": "Patient not found."}, 404

class PatientRegister(Resource):
    ''' Create Patient endpoint method '''
    arguments = reqparse.RequestParser()
    arguments.add_argument('name', type=str, required=True, help="The field 'name' cannot be left blank.")
    arguments.add_argument('cpf')
    arguments.add_argument('birthdate')
    arguments.add_argument('phone')
    arguments.add_argument('sus_card')

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        print('Patient was instantiated')
        self.repo = PatientRepository(conn)

    def post(self):
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


        





















    # def get(self, info): # all patients and his appointments method 1
    #     ''' Get all patients with "info" and his appointments '''
    #     response_patient = self.repo.find_patient(info)
    #     response_appointments = self.repo.find_appointments(info)

    #     result = []
    #     for patient in response_patient:

    #         appointments = []
    #         for appointment in response_appointments:

    #             json_appointment = {
    #                 'patient_name': appointment.patient_name,
    #                 'appointment_date': str(appointment.appointment_date),
    #                 'patient_attended': appointment.patient_attended,
    #                 'doctor_name': appointment.doctor_name
    #             }
    #             appointments.append(json_appointment)

    #         json_info = {
    #             'name': patient.name,
    #             'birthdate': str(patient.birthdate),
    #             'cpf': patient.cpf,
    #             'phone': patient.phone,
    #             'sus_card': patient.sus_card,
    #             'appointments': appointments
    #         }
    #         result.append(json_info)

    #     if result:
    #         return result
    #     return {'message': 'user not found'}, 404

    # def get(self, info): # all patients and his appointments method 2
    #     ''' Get all patients with "info" and his appointments '''
    #     response_patient = self.repo.find_patient(info)
    #     response_appointments = self.repo.find_appointments(info)

    #     result = []
    #     appointments = []

    #     for appointment in response_appointments:
    #         json_appointment = {
    #             'patient_name': appointment.patient_name,
    #             'appointment_date': str(appointment.appointment_date),
    #             'patient_attended': appointment.patient_attended,
    #             'doctor_name': appointment.doctor_name
    #         }
    #         appointments.append(json_appointment)

    #     for patient in response_patient:
    #         json_patient = {
    #             'name': patient.name,
    #             'birthdate': str(patient.birthdate),
    #             'cpf': patient.cpf,
    #             'phone': patient.phone,
    #             'sus_card': patient.sus_card,
    #             'appointments': appointments
    #         }
    #         result.append(json_patient)

    #     if result:
    #         return result
    #     return {'message': 'user not found'}, 404















    # # def put(self, paciente_id, option=5):
        
    # #     url = db_config["URI"]
    # #     engine = banco.create_engine(url, {})
    # #     Session = sessionmaker(bind=engine)
    # #     session = Session()

    # #     if option == 5: # jeito correto, só falta formatar.
    # #         response = session.query(PacienteModel).filter(PacienteModel.id == paciente_id).first() # retorna resultado
    # #         #response = session.query(PacienteModel).all() # retorna lista de resultados
    # #         if response:
    # #             return str(response.nome)
    # #         else:
    # #             return "not found", 404

