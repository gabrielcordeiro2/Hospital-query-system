import datetime
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from config.blacklist import BLACKLIST
from config.database import create_db, db_config
from models.entities import *
from resources.appointment import Appointment, AppointmentRegister, AppointmentUpdate
from resources.patient import Patient, PatientRegister
from resources.stay import Stay, StayRegister, StayUpdate
from resources.user import UserLogin, UserLogout, UserRegister

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = db_config["URI"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'DontTellAnyone'
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(days=14)
app.config['JWT_BLACKLIST_ENABLED'] = True

jwt = JWTManager(app)

@jwt.token_in_blocklist_loader
def verify_blacklist(self, token):
    return token['jti'] in BLACKLIST

@jwt.revoked_token_loader
def access_token_invalidated(jwt_header, jwt_payload):
    return {'message': 'You have been logged out.'}, 401 # Unauthorized

api = Api(app)
api.add_resource(Patient, '/patient/<string:info>')
api.add_resource(PatientRegister, '/patient/register')
api.add_resource(Appointment, '/appointment/<string:info>')
api.add_resource(AppointmentRegister, '/appointment/schedule')
api.add_resource(AppointmentUpdate, '/appointment/<string:appointment_id>')
api.add_resource(Stay, '/stay/<string:info>')
api.add_resource(StayRegister, '/stay/register')
api.add_resource(StayUpdate, '/stay/<string:stay_id>')
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')

if __name__ == "__main__":
    create_db()
    app.run(debug=True)
