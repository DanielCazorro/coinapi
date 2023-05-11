import requests

apikey = 'USE YOUR APIKEY'
api_url = 'http://rest-sandbox.coinapi.io'
# api_url = 'http://rest.coinapi.io'
endpoint = '/v1/exchangerate'

headers = {
    'X-CoinAPI-Key': apikey
}


# Pedir moneda origen: BTC
# Pedir moneda destino: EUR
# Preguntar el cambio a la API
# {'time': '2023-03-14T21:21:23.0000000Z', 'asset_id_base': 'BTC', 'asset_id_quote': 'EUR', 'rate': 22725.837234875708}
# Recoger el dato
# Mostrar un mensaje "Un XXX vale lo mismo que NNN YYY"
#                    "Un BTC vale lo mismo que 23000 EUR"
# Preguntar: ¿Quieres consultar de nuevo? (S/N)

seguir = 's'

while seguir.lower() == 's':
    # vista
    moneda_origen = input('¿Qué moneda quieres cambiar? ')
    moneda_destino = input('¿Qué moneda deseas obtener? ')
    # end vista

    # modelo
    url = f'{api_url}{endpoint}/{moneda_origen}/{moneda_destino}'
    response = requests.get(url, headers=headers)
    exchange = response.json()
    rate = exchange.get("rate")
    # end modelo

    # vista
    print(f'Un {moneda_origen} vale lo mismo que {rate:,.2f} {moneda_destino}')
    # end vista

    # controlador
    seguir = ''
    while seguir.lower() not in ('s', 'n'):
        seguir = input('¿Quieres consultar de nuevo? (S/N) ')
    # end controlador
