from typing import List, Optional
from sqlmodel import Session, select
from model.models import Endereco
from model.dto import EnderecoCreate

class EnderecoRepository:
    def __init__(self, session: Session):
        self.session = session

    def list(self, offset: int = 0, limit: int = 100) -> List[Endereco]:
        return list(self.session.exec(select(Endereco).offset(offset).limit(limit)).all())

    def get(self, endereco_id: int) -> Optional[Endereco]:
        return self.session.get(Endereco, endereco_id)

    def get_by_dono(self, dono: int) -> Optional[Endereco]:
        return self.session.exec(select(Endereco).where(Endereco.dono == dono)).all()

    def create(self, data: EnderecoCreate) -> Endereco:
        endereco = Endereco.model_validate(data)
        self.session.add(endereco)
        self.session.commit()
        self.session.refresh(endereco)
        return endereco