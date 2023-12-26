from sqlalchemy.orm import Session
from infra.sqlalchemy.model import model
from schemas import schemas
from infra.sqlalchemy.model.model import Serie

class repositorioSerie():
    def __init__(self, db: Session) -> None:
        self.db = db
        
    def criarSerie(self, serie: schemas.Serie):
        serie = model.Serie(titulo=serie.titulo, genero=serie.genero, lancamento=serie.lancamento,
                            qtdtemp=serie.qtdtemp, user_id=serie.user_id)
        
        self.db.add(serie)
        self.db.commit()
        self.db.refresh(serie)
        return serie
    
    def listarSerie(self):
        series = self.db.query(Serie).all()
        return series
    
    def listarId(self, id: int):
        serie = self.db.query(Serie).get(id)
        return serie
    
    def atualizarSerie(self,id: int, titulo:str, ano:int, genero: str, qtdtemp:int):
        serie = self.db.get(Serie, id)
        
        serie.titulo = titulo
        serie.ano = ano
        serie.genero = genero
        serie.qtdtemp = qtdtemp
        
        self.db.add(serie)
        self.db.commit()
        self.db.refresh(serie)
        return serie
    
    def deletarSerie(self, id:int):
        serie = self.db.get(Serie, id)
        
        self.db.delete(serie)
        self.db.commit()
        return serie