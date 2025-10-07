from model.models import PessoaBase, EnderecoBase
from typing import List, Optional
from sqlmodel import Field

class PessoaPublica(PessoaBase):
    id:int
    endereco: List["EnderecoPublico"] = []
    model_config = {"from_attributes": True}

class PessoaUpdate(PessoaBase):
    name: str = Field(default=None ,min_length=2, max_length=120)
    email: str = Field(default=None, index=True)
    
class EnderecoCreate(EnderecoBase):
    dono: int | None = Field(default=None, foreign_key="pessoa.id")

class EnderecoPublico(EnderecoBase):
    id: int
    model_config= {"from_attributes": True}