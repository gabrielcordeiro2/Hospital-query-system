from flask import Flask
from models.paciente import PacienteModel
from models.consulta import ConsultaModel
from models.internacao import InternacaoModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if __name__ == "__main__":
    from config.orm_banco import banco
    banco.init_app(app)
    banco.create_all(app=app)