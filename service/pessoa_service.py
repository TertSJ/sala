from fastapi import HTTPException, status
from typing import List
from sqlmodel import Session
from model.models import Pessoa
from model.dto import PessoaBase, PessoaPublica, PessoaUpdate
from repository.pessoa_repository import PessoaRepository
from repository.endereco_repository import EnderecoRepository

class PessoaService:
    def __init__(self, session: Session):
        self.repo = PessoaRepository(session)
        self.aux = EnderecoRepository(session)

    def create(self, payload: PessoaBase) -> PessoaPublica:
        if self.repo.get_by_email(payload.email):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="E-mail cadastrado anteriormente no sistema!")
        pessoa = self.repo.create(payload)
        return PessoaPublica.model_validate(pessoa)

    def list(self, offset: int, limit: int) -> List[PessoaPublica]:
        pessoas = self.repo.list(offset, limit)
        return [PessoaPublica.model_validate(h) for h in pessoas]

    def get(self, pessoa_id: int) -> PessoaPublica:
        pessoa = self.repo.get(pessoa_id)
        if not pessoa:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pessoa não encontrada")
        pessoa.endereco = self.aux.get_by_dono(pessoa_id)
        return PessoaPublica.model_validate(pessoa)

    def update(self, pessoa_id: int, payload: PessoaUpdate) -> PessoaPublica:
        pessoa = self.repo.get(pessoa_id)
        if not pessoa:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pessoa não encontrada")
        if self.repo.get_by_email(payload.email):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="E-mail cadastrado anteriormente no sistema!")
        pessoa = self.repo.update(pessoa, payload)
        return PessoaPublica.model_validate(pessoa)

    def delete(self, pessoa_id: int) -> None:
        pessoa = self.repo.get(pessoa_id)
        if not pessoa:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pessoa não encontrada")
        self.repo.delete(pessoa)