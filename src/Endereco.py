class Endereco:
    def __init__(self, cep, logradouro, bairro, cidade, estado):
        self.cep = cep
        self.logradouro = logradouro
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado

    def __str__(self):
        return (f"CEP: {self.cep}\nLogradouro: {self.logradouro}\n"
                f"Bairro: {self.bairro}\nCidade: {self.cidade}\nEstado: {self.estado}")
