from pydantic import BaseModel
from typing import Optional

class Serie(BaseModel):
    
    __tablename__ = "Serie"
    
    id: Optional[str] = None
    titulo: str
    genero: str
    lancamento: int
    qtdtemp: int