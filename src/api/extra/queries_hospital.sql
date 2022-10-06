/* ----------- repository/appointment - find_appointments() ----------------------*/

select
	p.id,
	p.name as patient_name,
	a.appointment_date,
	a.patient_attended,
	e.name as doctor_name
from appointments as a
join patients as p 
on p.id = a.patient_id
join employees as e 
on e.id = a.doctor_id 
where
	p.name = 'Chris Johnson' or
	p.cpf = '357386166775' or
	p.sus_card = '056921307982040668';

/* ----------- repository/appointment - schedule_appointment() -----------------*/

insert into appointments (
	appointment_date,
	patient_id,
	doctor_id,
	patient_attended,
	drug_allergy,
	description
)
values (
	'2099-11-29 12:31:15.000',
	1,
	3,
	true,
	'paracetamol',
	'Lorem Ipsum Description'
);

/* ----------- repository/appointment - update_appointment_info() ------------*/

update appointments
set
	patient_id = '3',
	appointment_date = '2300-10-18 10:11:10',
	patient_attended = true,
	doctor_id = '4',
	modified_in = now() 
where id = '118';
	
/* ----------- repository/appointment - find_appointment_id() ---------------*/

select id
from appointments
where id = '49';

/* ----------- repository/employee - find_doctor_id() -----------------------*/

select id
from employees
where "name" = 'Lucas de Paula Barros';

/* ----------- repository/employee - register_user() ------------------------*/

insert into employees(
	"name",
	"user",
	"password",
	"type"
)
values (
	'Roberto Gomes',
	'roberto23',
	sha256('12abc3'),
	'doctor'
);

/* ----------- repository/employee - find_by_login() ----------------------*/

select "user" 
from employees
where "user" = 'alvava2648';

/* ----------- repository/employee - find_password() ----------------------*/

select "password"
from employees
where "user" = 'lucas68';

/* ----------- repository/patient - find_patient() -----------------------*/

select
	p."name",
	p.birthdate,
	p.cpf,
	p.phone,
	p.sus_card
from patients p
where
	p."name" = 'Michelle Wiggins' or
	p.cpf = '253514484188' or
	p.sus_card = '762672615609155778';

/* ----------- repository/patient - find_patient_id() -------------------*/

select id
from patients p
where
	p."name" = 'Tony Weaver' or
	p.cpf = '244858882286' or
	p.sus_card = '924207197638558932';

/* ----------- repository/patient - register_patient() ------------------*/

insert into patients (
	"name",
	cpf,
	birthdate,
	phone,
	sus_card
)
values (
	'Julio Bento Gonzalo',
	'39224574805',
	'2001-01-11',
	'19989356624',
	'1256879243564'
);

/* ----------- repository/patient - update_patient_info() --------------*/
update patients 
set 
	cpf = '4521689532',
	birthdate = '2612-02-12',
	phone = '65482154636',
	sus_card = '56487213064121215'
where name = 'Andrea Greene';

/* ----------- repository/stay - find_stay() --------------------------*/
select 
	s.id as stay_id,
	s.stay_date,
	p."name" as patient_name,
	e."name" as doctor_name,
	s.status,
	s.room,
	s.bed
from stay s
join patients p 
on p.id = s.patient_id
join employees e
on e.id = s.doctor_id
where p.id = '49';

/* ----------- repository/stay - register_stay() ----------------------*/
insert into stay (
	stay_date,
	patient_id,
	doctor_id,
	drug_allergy,
	description,
	status,
	room,
	bed,
	modified_in
)
values (
	'2099-11-29 12:31:15',
	'3',
	'4',
	'paracetamol',
	'Its just a Lorem Ipsum description',
	'admitted',
	'A8',
	'5',
	now()
);

/* ----------- repository/stay - update_stay() ----------------------*/
update stay
set
	stay_date = '2001-01-01 01:01:01',
	patient_id = '3',
	doctor_id = '4',
	drug_allergy = 'paracetamol, dipirona',
	description = 'New description',
	status = 'observation',
	room = 'V2',
	bed = '3',
	modified_in = now()
where id = '118';

/* ----------- repository/stay - find_stay_id() ----------------------*/
select id
from stay
where id = '24';
