from sqlalchemy.orm import Session
from infra.sqlalchemy.model import model
from schemas import schemas

class repositorioSerie():
    def __init__(self, db: Session) -> None:
        self.db = db
        
    def criarSerie(self, serie: schemas.Serie):
        serie = model.Serie(titulo=serie.titulo, genero=serie.genero, lancamento=serie.lancamento,
                            qtdemp=serie.qtdtemp)
        
        self.db.add(serie)
        self.db.commit()
        self.db.refresh(serie)
        return serie
    
    def listarSerie(self):
        series = self.db.query().all()
        return series