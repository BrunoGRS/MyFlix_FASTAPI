from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from infra.sqlalchemy.config.database import Base
 
class Usuario(Base):
    
    __tablename__ = 'usuario'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String)
    senha = Column(String)
    series = relationship('Serie', back_populates='usuario')
    
class Serie(Base):
    
    __tablename__= 'serie'
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    genero = Column(String)
    lancamento = Column(Integer)
    qtdtemp = Column(Integer)
    user_id = Column(Integer, ForeignKey('usuario.id', name='fk_usuario'))
    
    usuario = relationship('Usuario', back_populates = 'series')
