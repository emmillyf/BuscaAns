from fastapi import status, HTTPException, Depends, APIRouter, Response
from sqlalchemy.orm import Session
from typing import List, Optional
from data.conexao import get_db 
from schemas.schema import OperadorasBase
import requests
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

@router.get("/operadoras/buscar/", response_model=List[OperadorasBase])
async def operadoras_by_filter(
    termo: Optional[str] = "", 
    pagina: int = 1, 
    por_pagina: int = 20, 
    db: Session = Depends(get_db)
):
    operadoras = service.get_by_filter(db, termo, pagina, por_pagina)
    
    if not operadoras:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nenhuma operadora encontrada para o termo pesquisado."
        )
    
    return operadoras

@router.get("/download-csv")
def download_csv():
    url = "https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/Relatorio_cadop.csv"
    r = requests.get(url)
    return Response(content=r.content, media_type="text/csv", headers={"Content-Disposition": "attachment; filename=operadoras_ativas.csv"})
