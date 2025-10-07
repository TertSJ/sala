from typing import List
from fastapi import HTTPException, status
from sqlmodel import Session
from model.dto import EnderecoCreate, EnderecoPublico
from repository.endereco_repository import EnderecoRepository
from repository.pessoa_repository import PessoaRepository

class EnderecoService:
    def __init__(self, session: Session):
        self.repo = EnderecoRepository(session)
        self.aux = PessoaRepository(session)

    def create(self, payload: EnderecoCreate) -> EnderecoPublico:
        pessoa = self.repo.get(payload.dono)
        if not pessoa:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pessoa não encontrada")
        endereco = self.repo.create(payload)
        return EnderecoPublico.model_validate(endereco)

    def list(self, offset: int, limit: int) -> List[EnderecoPublico]:
        enderecos = self.repo.list(offset, limit)
        return [EnderecoPublico.model_validate(e) for e in enderecos]

    def get(self, endereco_id: int) -> EnderecoPublico:
        endereco = self.repo.get(endereco_id)
        if not endereco:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="endereco nao cadastrado")
        # Retorna time com heróis aninhados
        return EnderecoPublico.model_validate(endereco)