from flask import jsonify
from flask_restful import Resource
from globals import importResource
from repository.patient import PatientRepository

conn = importResource('conn', 'config.database_instance')

class Patient(Resource):
    ''' Patient endpoint methods '''
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        print('Patient was instantiated')
        self.repo = PatientRepository(conn)

    def get(self, info):
        response1 = self.repo.find_patient(info)

        result = []
        for patient in response1:
            json_patient = {
                'name': patient.name,
                'nascimento': str(patient.birthdate),
                'cpf': patient.cpf,
                'telefone': patient.phone,
                'cartao_sus': patient.sus_card
            }
            result.append(json_patient)
        return result
















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

