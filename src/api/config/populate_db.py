from ..models import UserModel, PacienteModel, ConsultaModel, InternacaoModel
from config import banco, sessionmaker
from numpy.random import randint
from faker import Faker
import time

start_time = time.time()
fake = Faker()

def randomDate(start='-20y', end='now'):
    result = fake.date_between(
        start_date=start, end_date=end)
    return result

def randomDateTime(start='-20y', end='now'):
    result = fake.date_time_between(
        start_date=start, end_date=end)
    return result

def randomNum(n1, n2, length):
    nums = randint(n1, n2, length)
    result = ''.join(str(x) for x in nums)
    return result

def positiveNum(ndigits):
    while True:
        num = fake.random_number(digits=ndigits)
        if num > 0:
            return num

users = [
    UserModel(usuario="ana", senha="batata123", tipo="atendente"),
    UserModel(usuario="roberto19", senha="2468", tipo="enf_geral"),
    UserModel(usuario="julian4", senha="854abc", tipo="medico"),
    UserModel(usuario="lucas68", senha="hb8rh4", tipo="medico"),
    UserModel(usuario="antonio29", senha="sorvete27", tipo="medico")
]

pacientes = []
for _ in range(1000): # Pacientes
    paciente1 = PacienteModel(nome=fake.name(),
                              cpf=randomNum(0,10,12),
                              nascimento=randomDate(),
                              telefone=randomNum(0,10,12),
                              cartao_sus=randomNum(0,10,18))
    pacientes.append(paciente1)

consultas = []
for _ in range(1450): # Consultas
    if randint(0,9) != 0:
        modificado = fake.random.choice([randomDateTime(), None])
        medicamento = fake.random.choice([fake.word(), None])
        compareceu = fake.random.choice([True, False, True])
        descricao = fake.text(max_nb_chars=60)
        medico = fake.random.choice([3,4,5])

        consulta1 = ConsultaModel(data_consulta=randomDateTime(),
                                  paciente_compareceu=compareceu,
                                  medico_id=medico,
                                  paciente_id=positiveNum(3),
                                  alergia_medicamento=medicamento,
                                  descricao=descricao,
                                  modificado_em=modificado)
        consultas.append(consulta1)

internacoes = []
for _ in range(1000): # Internacoes
    if randint(0,9) == 0:
        status = fake.random.choice(["alta", "observacao", "internado"])
        quarto = f"{fake.random_letter().upper()}{positiveNum(2)}"
        modificado = fake.random.choice([randomDateTime(), None])
        medicamento = fake.random.choice([fake.word(), None])
        descricao = fake.text(max_nb_chars=60)
        medico = fake.random.choice([3,4,5])

        internacao1 = InternacaoModel(data_internacao=randomDateTime(),
                                      alergia_medicamento=medicamento,
                                      descricao=descricao,
                                      paciente_id=positiveNum(3),
                                      medico_id=medico,
                                      status=status,
                                      quarto=quarto,
                                      leito=positiveNum(1),
                                      modificado_em=modificado)
        internacoes.append(internacao1)

url = 'postgresql://postgres:123@localhost:5432'
engine = banco.create_engine(url, {})
Session = sessionmaker(bind=engine)
session = Session()

session.bulk_save_objects(users)
session.commit()
session.bulk_save_objects(pacientes)
session.commit()
session.bulk_save_objects(consultas)
session.commit()
session.bulk_save_objects(internacoes)
session.commit()
session.close()

print("Sucesso !!!")
delta_time = time.time() - start_time
print(f"A operação demorou {delta_time:.3f} segundos")
