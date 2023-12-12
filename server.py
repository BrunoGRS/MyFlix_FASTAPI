from infra.sqlalchemy.repository.serie import repositorioSerie
from fastapi import FastAPI, Depends
from infra.sqlalchemy.model.model import Serie
from uvicorn import run
from sqlalchemy.orm import Session
from infra.sqlalchemy.config.database import get_bd

app = FastAPI()

@app.post("/series/cadastrar")
async def cadSerie(serie: Serie, db: Session = Depends(get_bd)):
    serie = repositorioSerie(db).criarSerie(serie)
    await {'msg':'Serie Cadastrada com sucesso!'}

if __name__ == "__main__":
    run(app, port=8000)