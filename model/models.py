from typing import Optional, List
from sqlmodel import Field, SQLModel , Relationship


#-------------------------------Pessoa--------------------------------
class PessoaBase(SQLModel):
    name: str = Field(min_length=2, max_length=120)
    email: str = Field(index=True)
    

class Pessoa(PessoaBase, table=True):
    id: int | None = Field(default=None , primary_key=True)
    endereco: List["Endereco"] = Relationship(back_populates="endereco")
    


#-------------------------------Endereço-----------------------------
class EnderecoBase(SQLModel):
    logradouro : str = Field(default=None)
    numero : Optional[str] = None
    estado : str = Field(default=None)
    cidade : str = Field(default=None)
    bairro : str = Field(default=None)

class Endereco(EnderecoBase, table= True):
    id: int = Field(default=None, primary_key=True)
    dono: int | None = Field(default=None, foreign_key="pessoa.id")
    
