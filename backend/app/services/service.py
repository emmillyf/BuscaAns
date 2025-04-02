from models.model import operadoras_ans
from sqlalchemy import func
from sqlalchemy.orm import Session

def get_all(db: Session):
    return db.query(operadoras_ans).all()

def get_by_id(db: Session, operadora_id: int):
    return db.query(operadoras_ans).filter(operadoras_ans.registro_ans==operadora_id).first()

def get_by_filter(db: Session, termo: str, pagina: int = 1, por_pagina: int = 30):
    termo = termo.strip()  # Remove espaços em branco
    if not termo:
        return db.query(operadoras_ans).offset((pagina - 1) * por_pagina).limit(por_pagina).all()
    
    query = db.query(operadoras_ans).filter(

        operadoras_ans.nome_fantasia.ilike(f"%{termo}%") |
        operadoras_ans.cidade.ilike(f"%{termo}%") |
        operadoras_ans.uf.ilike(f"%{termo}%") |
        operadoras_ans.modalidade.ilike(f"%{termo}%")

    ).offset((pagina - 1) * por_pagina).limit(por_pagina)

    return query.all()
