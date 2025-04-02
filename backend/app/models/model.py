from sqlalchemy import Column, Integer, String
from data.conexao import Base

class operadoras_ans(Base):
    __tablename__ = "operadoras_plano_de_saude" 

    registro_ans = Column(Integer, primary_key=True, index=True)
    cnpj = Column(String(14), unique=True)
    nome_fantasia = Column(String(30), nullable=True)
    modalidade = Column(String(200))
    cidade = Column(String(200))
    uf = Column(String(10))
    cep = Column(String(10))
    ddd = Column(String(10))
    telefone = Column(String(20), nullable=True)
    endereco_eletronico = Column(String(50), nullable=True)
    representante = Column(String(120), nullable=True)
    data_registro_ans = Column(String(20), nullable=True)