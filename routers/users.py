from infra.sqlalchemy.repository.usuario import repositorioUsuario
from fastapi import Depends, status, APIRouter
from schemas.schemas import Usuario
from uvicorn import run
from typing import List
from sqlalchemy.orm import Session
from infra.sqlalchemy.config.database import get_bd

router = APIRouter()

@router.post("/usuarios/cadastrar", 
             status_code=status.HTTP_201_CREATED, response_model=dict,
             tags=["users"])
def criarUsuario(usuario: Usuario, db: Session = Depends(get_bd)):
    user = repositorioUsuario(db).criarUsuário(usuario)
    return {'msg':'Usuário criado com sucesso!'}

@router.get("/series/user/listar",status_code=status.HTTP_200_OK, 
            response_model=List[Usuario],
            tags=["users"])
def listarUser(db: Session = Depends(get_bd)):
    serie = repositorioUsuario(db).listarUser()
    return serie
