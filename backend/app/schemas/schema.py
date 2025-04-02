from pydantic import BaseModel 
class OperadorasBase(BaseModel):
    registro_ans: int
    nome_fantasia: str
    cnpj: str
    modalidade: str
    
    class Config:
        from_attributes = True

class OperadorasInformacoes(OperadorasBase):
    registro_ans: int
    nome_fantasia: str
    cnpj: str
    modalidade: str
    cidade: str
    uf: int
    cep: int
    ddd: int
    telefone: str
    endereco_eletronico: str
    representante: str
    data_registro_ans: str