from datetime import date, datetime
from config.orm_banco import banco

class PacienteModel(banco.Model):
    __tablename__ = 'pacientes'

    cpf = banco.Column(banco.String(12), primary_key=True)
    nome_completo = banco.Column(banco.String(70))
    # data_internacao = 
    # data_consulta = 
    # status =
    nascimento = banco.Column(banco.Date)
    telefone = banco.Column(banco.String(12))
    cartao_sus = banco.Column(banco.String(18))
    cor_da_pele = banco.Column(banco.String(10))
    # altura = 


    def __init__(self, cpf, nome_completo, nascimento, telefone, cartao_sus, cor_da_pele):
        self.cpf = cpf
        self.nome_completo = nome_completo
        self.nascimento = nascimento
        self.telefone = telefone
        self.cartao_sus = cartao_sus
        self.cor_da_pele = cor_da_pele    
