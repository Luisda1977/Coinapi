import requests


apikey = "92D803FB-637A-4A9E-83B5-15B457DF2C9B"
cabeceras = {
    "X-CoinApi-Key": apikey
}


seguir = "S"

while seguir.upper() == "S":
    moneda_origen = input("¿Qué moneda quieres cambiar?")
    moneda_destino = input("¿Qué moneda deseas obtener?")

    url = f"http://rest.coinapi.io/v1/exchangerate/{moneda_origen}/{moneda_destino}"
    respuesta = requests.get(url, headers=cabeceras)
    tipo_cambio = respuesta.json()

    # Un euro son xxxxx bitcoins
    # Un euro son xxxxx dólares
    # Un bitcoin son xx dólares

    cambio = tipo_cambio["rate"]
    print("Un {} vale como {:,.2f} {}".format(
        moneda_origen, cambio, moneda_destino))

    seguir = ""
    while seguir.upper() not in ("S", "N"):
        seguir = input("¿Quieres hacer más cambio de monedas? (S/N) ")
