# app/controllers/teams.py
from typing import List, Annotated
from fastapi import APIRouter, Depends, Query
from util.database import SessionDep
from model.dto import EnderecoCreate, EnderecoPublico
from service.endereco_service import EnderecoService

router = APIRouter(prefix="/endereco", tags=["Endereco"])

def get_endereco_service(session: SessionDep) -> EnderecoService:
    return EnderecoService(session)

ServiceDep = Annotated[EnderecoService, Depends(get_endereco_service)]

@router.post("/", response_model=EnderecoPublico, status_code=201)
def create_endereco(payload: EnderecoCreate, service: ServiceDep):
    return service.create(payload)

@router.get("/", response_model=List[EnderecoPublico])
def list_teams(
    service: ServiceDep,
    offset: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
):
    return service.list(offset, limit)

@router.get("/{endereco_id}", response_model=EnderecoPublico)
def get_endereco(endereco_id: int, service: ServiceDep):
    return service.get(endereco_id)