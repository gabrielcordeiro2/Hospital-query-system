from config import banco

class ConsultaModel(banco.Model):
    __tablename__ = 'consultas'

    id = banco.Column(banco.Integer, primary_key=True)
    data_consulta = banco.Column(banco.DateTime)
    paciente_id = banco.Column(banco.Integer, banco.ForeignKey('pacientes.id'))
    medico_id = banco.Column(banco.Integer, banco.ForeignKey('funcionarios.id'))
    paciente_compareceu = banco.Column(banco.Boolean)
    alergia_medicamento = banco.Column(banco.String(30))
    descricao = banco.Column(banco.Text)
    modificado_em = banco.Column(banco.DateTime)
