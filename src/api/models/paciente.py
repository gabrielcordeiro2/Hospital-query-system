from config import banco

class PacienteModel(banco.Model):
    __tablename__ = 'pacientes'

    id = banco.Column(banco.Integer, primary_key=True)
    nome = banco.Column(banco.String(60))
    cpf = banco.Column(banco.String(12), unique=True)
    nascimento = banco.Column(banco.Date)
    telefone = banco.Column(banco.String(12))
    cartao_sus = banco.Column(banco.String(18))
