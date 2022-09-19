from time import time
from faker import Faker
from numpy.random import randint
from config.database import DBConnection
from models.entities import *

start = time()
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

employees = [
    UserModel(user="ana", name="Ana Alves Toledo", password="batata123", type="attendant"),
    UserModel(user="roberto19", name="Roberto Padilha", password="2468", type="head_nurse"),
    UserModel(user="julian4", name="Julian Oliveira", password="854abc", type="doctor"),
    UserModel(user="lucas68", name="Lucas de Paula Barros", password="hb8rh4", type="doctor"),
    UserModel(user="antonio29", name="Antonio Benedito", password="sorvete27", type="doctor")
]

patients = []
for _ in range(1000): # Pacientes
    patient1 = PatientModel(
                    name=fake.name(),
                    cpf=randomNum(0,10,12),
                    birthdate=randomDate(),
                    phone=randomNum(0,10,12),
                    sus_card=randomNum(0,10,18))
    patients.append(patient1)

appointments = []
for _ in range(1450): # Consultas
    if randint(0,9) != 0:
        modified = fake.random.choice([randomDateTime(), None])
        drug = fake.random.choice([fake.word(), None])
        attended = fake.random.choice([True, False, True])
        description = fake.text(max_nb_chars=60)
        doctor = fake.random.choice([3,4,5])

        appointment1 = AppointmentModel(
                            appointment_date=randomDateTime(),
                            patient_attended=attended,
                            doctor_id=doctor,
                            patient_id=positiveNum(3),
                            drug_allergy=drug,
                            description=description,
                            modified_in=modified)
        appointments.append(appointment1)

stay = []
for _ in range(1000): # Stay
    if randint(0,9) == 0:
        status = fake.random.choice(["discharged", "observation", "admitted"])
        room = f"{fake.random_letter().upper()}{positiveNum(2)}"
        modified = fake.random.choice([randomDateTime(), None])
        drug = fake.random.choice([fake.word(), None])
        description = fake.text(max_nb_chars=60)
        doctor_id = fake.random.choice([3,4,5])

        stay1 = StayModel(
                        stay_date=randomDateTime(),
                        drug_allergy=drug,
                        description=description,
                        patient_id=positiveNum(3),
                        doctor_id=doctor_id,
                        status=status,
                        room=room,
                        bed=positiveNum(1),
                        modified_in=modified)
        stay.append(stay1)


with DBConnection() as db:
    db.session.bulk_save_objects(employees)
    db.session.commit()
    db.session.bulk_save_objects(patients)
    db.session.commit()
    db.session.bulk_save_objects(appointments)
    db.session.commit()
    db.session.bulk_save_objects(stay)
    db.session.commit()
    db.session.close()

delta = time() - start
print("Success !!!")
print(f"The operation took {delta:.3f} seconds")
