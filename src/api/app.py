from flask import Flask
from flask_restful import Api
from globals import importResource
from config.database import Base, db_config
from models.entities import *
from resources.patient import Patient, PatientRegister
from resources.appointment import Appointment, AppointmentRegister, AppointmentUpdate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = db_config["URI"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
conn = importResource('conn', 'config.database_instance')
api.add_resource(Patient, '/patient/<string:info>')
api.add_resource(PatientRegister, '/patient/register')
api.add_resource(Appointment, '/appointment/<string:info>')
api.add_resource(AppointmentRegister, '/appointment/schedule')
api.add_resource(AppointmentUpdate, '/appointment/<string:appointment_id>')

if __name__ == "__main__":

    Base.metadata.create_all(conn.create_engine()) # Create DB
    app.run(debug=True)
