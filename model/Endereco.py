class Endereco:
    logradouro : str
    numero : str
    estado : str
    cidade : str
    bairro : str

    def __init__(self,logradouro : str ,numero : str , estado : str , cidade : str , bairro : str):
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.logradouro = logradouro
        self.estado = estado
        self.numero = numero
    