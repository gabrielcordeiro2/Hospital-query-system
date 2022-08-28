from config.orm_banco import banco

class InternacaoModel(banco.Model):
    __tablename__ = 'internacoes'

    data_internacao = banco.Column(banco.DateTime, primary_key=True)
    internacao_id = banco.Column(banco.Integer)
    paciente_nome = banco.Column(banco.String(70))
    medico = banco.Column(banco.String(18))
    alergia_medicamento = banco.Column(banco.String(10))
    status = banco.Column(banco.String(20)) 