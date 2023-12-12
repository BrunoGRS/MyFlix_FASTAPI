from sqlalchemy import Column, Integer, String
from infra.sqlalchemy.config.database import Base

class Serie(Base):
    
    __tablename__= "Serie"
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    genero = Column(String)
    lancamento = Column(Integer)
    qtdtemp = Column(Integer)