from flask import Flask
from flask_restful import Api
from config.database import db_config, create_db
from models.entities import *
from resources.patient import Patient, PatientRegister
from resources.appointment import Appointment, AppointmentRegister, AppointmentUpdate
from resources.stay import Stay, StayRegister, StayUpdate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = db_config["URI"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
api.add_resource(Patient, '/patient/<string:info>')
api.add_resource(PatientRegister, '/patient/register')
api.add_resource(Appointment, '/appointment/<string:info>')
api.add_resource(AppointmentRegister, '/appointment/schedule')
api.add_resource(AppointmentUpdate, '/appointment/<string:appointment_id>')
api.add_resource(Stay, '/stay/<string:info>')
api.add_resource(StayRegister, '/stay/register')
api.add_resource(StayUpdate, '/stay/<string:stay_id>')

if __name__ == "__main__":
    create_db()
    app.run(debug=True)
