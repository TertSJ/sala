from fastapi import APIRouter, Query, Depends
from typing import List, Annotated
from util.database import SessionDep
from model.dto import PessoaBase, PessoaUpdate, PessoaPublica
from service.pessoa_service import PessoaService

router = APIRouter(prefix="/pessoas", tags=["Pessoas"])

def get_pessoa_service(session: SessionDep) ->PessoaService:
    return PessoaService(session)

ServiceDep = Annotated[PessoaService, Depends(get_pessoa_service)]

@router.post("/", response_model=PessoaPublica, status_code=201)
def create_pessoa(pessoa: PessoaBase, service: ServiceDep):
    return service.create(pessoa)

@router.get("/", response_model=List[PessoaPublica])
def read_pessoas(
    service: ServiceDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    return service.list(offset, limit)

@router.get("/{pessoa_id}", response_model=PessoaPublica)
def read_pessoa(pessoa_id: int, service: ServiceDep):
    return service.get(pessoa_id)

@router.patch("/{pessoa_id}", response_model=PessoaPublica)
def update_pessoa(pessoa_id: int, pessoa: PessoaUpdate, service: ServiceDep):
    return service.update(pessoa_id, pessoa)

@router.delete("/{pessoa_id}", status_code=204)
def delete_pessoa(pessoa_id: int, service: ServiceDep):
    service.delete(pessoa_id)
    return None