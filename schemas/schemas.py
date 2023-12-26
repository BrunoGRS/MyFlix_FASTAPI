from pydantic import BaseModel
from typing import Optional, List

class Serie(BaseModel):
    
    __tablename__= "Serie"
    
    id: Optional[int] = None
    titulo: str
    genero: str
    lancamento: int
    qtdtemp: int
    user_id:Optional[int]
    
    class Config:
        orm_mode = True
        
class Usuario(BaseModel):
    
    __tablename__ = "Usuario"
    
    id: Optional[int] = None
    nome: str
    email: str
    senha: str
    series: List[Serie] = []
    
    class Config:
        orm_mode = True