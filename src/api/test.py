from globals import importResource
from repository.patient import PatientRepository
from repository.employee import EmployeeRepository
from repository.stay import StayRepository
conn = importResource('conn', 'config.database_instance')
from datetime import datetime

now = datetime.now()

repo = PatientRepository(conn)
repo2 = EmployeeRepository(conn)
repo3 = StayRepository(conn)

# print(repo.schedule_appointment(
#     appointment_date='9999-10-11 06:06:06.000',
#     patient_id='1',
#     doctor_id='4',
#     patient_attended=None,
#     drug_allergy=None,
#     description=None
# ))

# print(repo.find_patient_id('764850576866602326'))

# print(repo2.find_doctor_id('Lucas de Paula Barros'))

# print(repo.schedule_appointment(
#     appointment_date='1111-06-06 06:06:06',
#     patient_id='7',
#     doctor_id='3'
# ))

# print(repo.find_appointment_id(
#     patient_id='16',
#     date='2016-09-14 14:44:38',
#     doctor_id='5'
# ))

# print(repo.update_appointment_info(
#     appointment_id='10',
#     patient_id='16',
#     date='9999-09-14 14:44:38',
#     doctor_id='5'
# ))

# print(repo.update_patient_info(
#     info='221459126260',
#     name='Cynthia Gardner',
#     cpf='123456789',
#     birthdate='2999-12-12',
#     phone='19989347713',
#     sus_card='15975246'
# ))

# print(repo.find_appointment_id(
#     appointment_id='8935'
# ))



# id 27 -> Christopher Phillips

#print(repo3.find_stay('4'))
# print(repo3.register_stay(
#     stay_date='2444-04-04 04:04:04',
#     patient_id='4',
#     doctor_id='3',
#     drug_allergy=None,
#     description='Any Lorem Ipsum',
#     status='admitted',
#     room='B6',
#     bed='4'
# ))

# print(repo3.update_stay_info(
#     stay_id='190',
#     stay_date='2888-08-08 05:05:05',
#     patient_id='592',
#     doctor_id='4',
#     status='observation',
#     room='B8',
#     bed='3'
# ))

# print(repo3.find_stay_id(222))

# print(repo2.register_user(
#     name='gabriel',
#     user='gabriel27',
#     password='1234a'
# ))

#print(repo2.find_by_login('gabriel27').user)



from werkzeug.security import generate_password_hash, check_password_hash

# p1 = generate_password_hash(password='123456', method='sha256')


# p3 = '123456'

# print(len((p1)))
# print(check_password_hash(p1, p3))

a = repo2.find_password('ana').password
b = check_password_hash(a, 'batata123')

print(b)