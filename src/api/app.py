from flask import Flask
from models import ConsultaModel, InternacaoModel, PacienteModel, UserModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if __name__ == "__main__":
    from config import banco
    banco.init_app(app)
    banco.create_all(app=app)
    app.run(debug=True)
