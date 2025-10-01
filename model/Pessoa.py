from model.Endereco import Endereco

class Pessoa:
    nome : str
    email : str
    idade: int
    endereco : list


    def __init__(self, nome:str, idade: int, email:str, endereco: list) -> None:
        self.nome = nome
        self.email = email
        self.idade = idade
        self.endereco.copy(endereco)
        
        

    
