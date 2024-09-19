import requests
from Endereco import Endereco

import requests

class ApiService:
    def procurar_cep(self, cep):
        try:
            response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
            response.raise_for_status()
            return response.json() 
        except requests.RequestException:
            return None




    