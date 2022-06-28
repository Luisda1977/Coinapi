import requests


apikey = "92D803FB-637A-4A9E-83B5-15B457DF2C9B"
cabeceras = {
    "X-CoinApi-Key": apikey
}

moneda_origen = input("¿Qué moneda quieres cambiar?")
moneda_destino = input("¿Qué moneda deseas obtener?")

url = f"http://rest.coinapi.io/v1/exchangerate{moneda_origen}/{moneda_destino}"
respuesta = requests.get(url, headers=cabeceras)
