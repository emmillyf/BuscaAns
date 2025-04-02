from models.model import operadoras_ans
from sqlalchemy.orm import Session

def get_all(db: Session):
    return db.query(operadoras_ans).all()

def get_by_id(db: Session, operadora_id: int):
    return db.query(operadoras_ans).filter(operadoras_ans.registro_ans==operadora_id).first()