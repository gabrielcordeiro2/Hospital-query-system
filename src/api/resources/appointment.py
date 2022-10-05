from typing import List
from flask_restful import Resource, reqparse
from globals import importResource
from repository.employee import EmployeeRepository
from repository.patient import PatientRepository
from repository.appointment import AppointmentRepository
from flask_jwt_extended import jwt_required

conn = importResource("conn", "config.database_instance")

def resource_arguments():
    arguments = reqparse.RequestParser()
    arguments.add_argument(
        "appointment_date",
        type=str,
        required=True,
        help="The field 'appointment_date' cannot be left blank.",
    )
    arguments.add_argument(
        "patient_info",
        type=str,
        required=True,
        help="The field 'patient_id' cannot be left blank.",
    )
    arguments.add_argument(
        "doctor_name",
        type=str,
        required=True,
        help="The field 'doctor_id' cannot be left blank.",
    )
    arguments.add_argument("patient_attended", default=None, type=bool)
    arguments.add_argument("drug_allergy", default=None, type=str)
    arguments.add_argument("description", default=None, type=str)
    return arguments

class Appointment(Resource):
    ''' Find Appointments info endpoint methods '''
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        print("Appointment was instantiated")
        self.repo = AppointmentRepository(conn)

    @jwt_required()
    def get(self, info: str) -> List:
        response = self.repo.find_appointments(info)
        result = []

        for appointment in response:
            json_appointment = {
                "Appointment_id": str(appointment.id),
                "patient_name": appointment.patient_name,
                "appointment_date": str(appointment.appointment_date),
                "patient_attended": appointment.patient_attended,
                "doctor_name": appointment.doctor_name,
            }
            result.append(json_appointment)

        if result:
            return result
        return {"message": "Appointment not found"}, 404

class AppointmentRegister(Resource):
    ''' Create Appointment endpoint method '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("Appointment was instantiated")
        self.repo = PatientRepository(conn)
        self.repo2 = EmployeeRepository(conn)
        self.repo3 = AppointmentRepository(conn)
        self.arguments = resource_arguments()

    @jwt_required()
    def post(self):
        data = self.arguments.parse_args()
        patient_found = self.repo.find_patient_id(data.get('patient_info'))
        doctor_found = self.repo2.find_doctor_id(data.get('doctor_name'))

        if patient_found and doctor_found:
            self.repo3.schedule_appointment(
                patient_id=patient_found.id,
                doctor_id=doctor_found.id,
                appointment_date=data.get('appointment_date'),
                patient_attended=data.get('patient_attended'),
                drug_allergy=data.get('drug_allergy'),
                description=data.get('description')
            )
            return {'message': 'Appointment successfully scheduled!'}, 201
        return {'message': 'Error, patient or doctor information not found.'}, 404

class AppointmentUpdate(Resource):
    ''' Update Appointment endpoint method '''
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        print("Appointment was instantiated")
        self.repo = PatientRepository(conn)
        self.repo2 = EmployeeRepository(conn)
        self.repo3 = AppointmentRepository(conn)
        self.arguments = resource_arguments()

    jwt_required()
    def put(self, appointment_id):
        data = self.arguments.parse_args()
        patient_found = self.repo.find_patient_id(data.get('patient_info'))
        doctor_found = self.repo2.find_doctor_id(data.get('doctor_name'))
        
        if patient_found and doctor_found:
            appointment_found = self.repo3.find_appointment_id(appointment_id)
            if appointment_found:
                self.repo3.update_appointment_info(
                    appointment_id=appointment_found.id,
                    patient_id=patient_found.id,
                    doctor_id=doctor_found.id,
                    date=data.get('appointment_date')
                )
                return {'message': 'Appointment updated successfully!'}, 200
            return {'message': 'Error, Appointment not found.'}, 404
        return {'message': 'Error, patient or doctor information not found.'}, 404 
