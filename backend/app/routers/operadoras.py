from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from data.conexao import get_db 
from schemas.schema import OperadorasBase
import services.service as service

router = APIRouter(
)

@router.get("/operadoras/", response_model=List[OperadorasBase])
async def listar_operadoras(db: Session = Depends(get_db)):
    lista_operadoras = service.get_all(db)
    if not lista_operadoras:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return lista_operadoras

@router.get("/operadoras/{id}", response_model=OperadorasBase)
async def operadora_by_id(id:int, db: Session = Depends(get_db)):
    operadora_queryset = service.get_by_id(db, id)
    if not operadora_queryset:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return operadora_queryset
