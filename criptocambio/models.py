# Operaciones de negocio y acceso a la API CoinAPI
import requests

from . import APIKEY

api_url = 'http://rest-sandbox.coinapi.io'
endpoint = '/v1/exchangerate'
headers = {
    'X-CoinAPI-Key': APIKEY
}

# Manejo de errores de la API
class APIError(Exception):
    pass

# Modelo para gestionar las consultas de cambio de moneda
class CriptoModel:
    """
    - constructor
    - moneda origen
    - moneda destino
    - cambio
    - método consultar cambio
    """

    origen = ''
    destino = ''

    def __init__(self):
        self.cambio = 0.0

    def consultar_cambio(self):
        # Construcción de la URL para la consulta de cambio
        url = f'{api_url}{endpoint}/{self.origen}/{self.destino}'
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            # Si la respuesta es exitosa, obtiene el tipo de cambio
            exchange = response.json()
            self.cambio = exchange.get("rate")
        else:
            # En caso de error en la respuesta de la API, se lanza una excepción
            raise APIError(
                f'Error {response.status_code} {response.reason} al consultar la API'
            )
