from config.orm_banco import banco

class ConsultaModel(banco.Model):
    __tablename__ = 'consultas'

    data_consulta = banco.Column(banco.DateTime, primary_key=True)
    consulta_id = banco.Column(banco.Integer)
    paciente_nome = banco.Column(banco.String(70))
    paciente_compareceu = banco.Column(banco.Boolean)
    medico = banco.Column(banco.String(18))
    cpf = banco.Column(banco.String(12))
    altura = banco.Column(banco.Float)
    alergia_medicamento = banco.Column(banco.String(10))