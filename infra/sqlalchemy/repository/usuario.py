from sqlalchemy.orm import Session
from schemas import schemas
from infra.sqlalchemy.model.model import Usuario
from infra.sqlalchemy.model.model import Serie

class repositorioUsuario():
    def __init__(self, db: Session) -> None:
        self.db = db
        
    def criarUsuário(self, usuario: Usuario):
        user = Usuario(nome=usuario.nome, email=usuario.email, senha=usuario.senha)
        
        self.db.add	(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def listarUser(self):
        serie = self.db.query(Usuario).all()
        return serie