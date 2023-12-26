from infra.sqlalchemy.repository.serie import repositorioSerie
from fastapi import Depends, status, APIRouter
from schemas.schemas import Serie
from uvicorn import run
from typing import List
from sqlalchemy.orm import Session
from infra.sqlalchemy.config.database import get_bd

router = APIRouter()

@router.post("/series/cadastrar", status_code=status.HTTP_201_CREATED, 
             response_model=dict, tags=["series"])
def cadSerie(serie: Serie, db: Session = Depends(get_bd)):
    serie = repositorioSerie(db).criarSerie(serie)
    return {'msg':'Serie Cadastrada com sucesso!'}

@router.get("/series/listar", status_code=status.HTTP_200_OK, 
            response_model=List[Serie], tags=["series"])
def listarSerie(db: Session = Depends(get_bd)):
    series = repositorioSerie(db).listarSerie()
    return series

@router.get("/series/listar/{id}", status_code=status.HTTP_200_OK, 
            response_model=Serie, tags=["series"])
def listarId(id: int, db: Session = Depends(get_bd)):
    serie = repositorioSerie(db).listarId(id)
    return serie

@router.post("/series/atualizar", status_code=status.HTTP_200_OK, 
             response_model=dict, tags=["series"])
def atualizarSerie(id: int, titulo:str, ano:int,genero:str, qtdtemp: int, db: Session = Depends(get_bd)):
    serie = repositorioSerie(db).atualizarSerie(id, titulo, ano, genero, qtdtemp)
    return {'msg':'Série atualizada com sucesso!'}

@router.delete("/serie/deletar/{id:int}", status_code=status.HTTP_200_OK, 
               response_model=dict, tags=["series"])
def deletarSerie(id: int, db: Session = Depends(get_bd)):
    serie = repositorioSerie(db).deletarSerie(id)
    return {"msg":"Série deletada com sucesso!"}
