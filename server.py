from infra.sqlalchemy.repository.serie import repositorioSerie
from infra.sqlalchemy.repository.usuario import repositorioUsuario
from fastapi import FastAPI, Depends, status
from schemas.schemas import Serie, Usuario
from uvicorn import run
from typing import List
from sqlalchemy.orm import Session
from infra.sqlalchemy.config.database import get_bd, create_bd
from fastapi.middleware.cors import CORSMiddleware

create_bd()

app = FastAPI()


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#SERIES
@app.post("/series/cadastrar", status_code=status.HTTP_201_CREATED, response_model=dict)
def cadSerie(serie: Serie, db: Session = Depends(get_bd)):
    serie = repositorioSerie(db).criarSerie(serie)
    return {'msg':'Serie Cadastrada com sucesso!'}

@app.get("/series/listar", status_code=status.HTTP_200_OK, response_model=List[Serie])
def listarSerie(db: Session = Depends(get_bd)):
    series = repositorioSerie(db).listarSerie()
    return series

@app.get("/series/listar/{id}", status_code=status.HTTP_200_OK, response_model=Serie)
def listarId(id: int, db: Session = Depends(get_bd)):
    serie = repositorioSerie(db).listarId(id)
    return serie

@app.post("/series/atualizar", status_code=status.HTTP_200_OK, response_model=dict)
def atualizarSerie(id: int, titulo:str, ano:int,genero:str, qtdtemp: int, db: Session = Depends(get_bd)):
    serie = repositorioSerie(db).atualizarSerie(id, titulo, ano, genero, qtdtemp)
    return {'msg':'Série atualizada com sucesso!'}

@app.delete("/serie/deletar/{id:int}", status_code=status.HTTP_200_OK, response_model=dict)
def deletarSerie(id: int, db: Session = Depends(get_bd)):
    serie = repositorioSerie(db).deletarSerie(id)
    return {"msg":"Série deletada com sucesso!"}


#USUÁRIOS
@app.post("/usuarios/cadastrar", status_code=status.HTTP_201_CREATED, response_model=dict)
def criarUsuario(usuario: Usuario, db: Session = Depends(get_bd)):
    user = repositorioUsuario(db).criarUsuário(usuario)
    return {'msg':'Usuário criado com sucesso!'}

@app.get("/series/user/listar", response_model=List[Usuario])
def listarUser(db: Session = Depends(get_bd)):
    serie = repositorioUsuario(db).listarUser()
    return serie

if __name__ == "__main__":
    run(app, port=8000)