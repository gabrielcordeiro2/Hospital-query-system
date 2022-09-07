from config import banco
import enum

class StatusType(enum.Enum):
    alta = "alta"
    observacao = "observacao"
    internado = "internado"

class InternacaoModel(banco.Model):
    __tablename__ = 'internacoes'

    id = banco.Column(banco.Integer, primary_key=True)
    data_internacao = banco.Column(banco.DateTime)
    paciente_id = banco.Column(banco.Integer, banco.ForeignKey('pacientes.id'))
    medico_id = banco.Column(banco.Integer, banco.ForeignKey('funcionarios.id'))
    alergia_medicamento = banco.Column(banco.String(30))
    descricao = banco.Column(banco.Text)
    status = banco.Column(banco.Enum(StatusType))
    quarto = banco.Column(banco.String(3))
    leito = banco.Column(banco.String(2))
    modificado_em = banco.Column(banco.DateTime)
