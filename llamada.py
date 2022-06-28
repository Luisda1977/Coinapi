import requests


apikey = "92D803FB-637A-4A9E-83B5-15B457DF2C9B"
cabeceras = {
    "X-CoinApi-Key": apikey
}
api_url = "http://rest-sandbox.coinapi.io"
endpoint = "/v1/exchanges"

url = api_url + endpoint

respuesta = requests.get(url, headers=cabeceras)
codigo = respuesta.status_code

if codigo == 200:
    print("El resultado de la consulta es:")
    print(respuesta.text)
else:
    print("La petición a la API ha fallado")
    print(f"Código de error {codigo}")
    print(f"Razón del error {respuesta.reason}")
    print(respuesta.text)
