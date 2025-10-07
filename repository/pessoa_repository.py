from sqlmodel import Session, select
from typing import List, Optional
from model.dto import PessoaBase, PessoaUpdate
from model.models import Pessoa

class PessoaRepository:
    def __init__(self, session: Session):
        self.session = session
    
    def list(self, offset: int = 0, limit: int = 100) -> List[Pessoa]:
        return list(self.session.exec(select(Pessoa).offset(offset).limit(limit)).all())
    
    def get(self, pessoa_id: int) -> Optional[Pessoa]:
        return self.session.get(Pessoa, pessoa_id)

    def get_by_name(self, name: str) -> Optional[Pessoa]:
        return self.session.exec(select(Pessoa).where(Pessoa.name == name)).first()
    
    def get_by_email(self, email: str) -> Optional[Pessoa]:
        return self.session.exec(select(Pessoa).where(Pessoa.email == email)).first()
    

    def create(self, data: PessoaBase) -> Pessoa:
        pessoa = Pessoa.model_validate(data)
        self.session.add(pessoa)
        self.session.commit()
        self.session.refresh(pessoa)
        return pessoa
    

    def update(self, pessoa: Pessoa, data: PessoaUpdate) -> Pessoa:
        update_data = data.model_dump(exclude_unset=True)
        for k, v in update_data.items():
            setattr(pessoa, k, v)
        self.session.add(pessoa)
        self.session.commit()
        self.session.refresh(pessoa)
        return pessoa
    
    def delete(self, pessoa: Pessoa) -> None:
        self.session.delete(pessoa)
        self.session.commit()