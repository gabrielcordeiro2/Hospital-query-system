from config import banco
import enum

class UserType(enum.Enum):
    atendente = "atendente"
    enf_geral = "enf_geral"
    medico = "medico"

class UserModel(banco.Model):
    __tablename__ = 'funcionarios'

    id = banco.Column(banco.Integer, primary_key=True)
    usuario = banco.Column(banco.String(10), nullable=False, unique=True)
    senha = banco.Column(banco.String(20), nullable=False)
    tipo = banco.Column(banco.Enum(UserType), nullable=False)
