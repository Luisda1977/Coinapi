import requests

from . import APIKEY


class APIError(Exception):
    pass


class CriptoModel:
    """
    -moneda_origen
    -moneda_destino
    -cambio
    -consultar cambio (método)
    """

    def __init__(self, origen, destino):
        """
        Construyendo un obejto con las monedas origen y destino
        y el cambio obtenido desde CoinApi inicializado a cero
        """
        self.moneda_origen = ""
        self.moneda_destino = ""
        self.cambio = 0.0

    def consultar_cambio(self):
        """
        -Consulta el cambio entre la mondesa origen y la moneda destino
        utlizando la API REST CoinApi
        """
        cabeceras = {
            "X-CoinApi-Key": APIKEY
        }
        url = f"http://rest.coinapi.io/v1/exchangerate/{self.moneda_origen}/{self.moneda_destino}"
        respuesta = requests.get(url, headers=cabeceras)

        if respuesta.status_code == 200:
            # guardo el cambio obtenido
            self.cambio = respuesta.json()["rate"]
        else:
            raise APIError("Ha ocurrido un error {} {} al consultar la API.".format(
                respuesta.status_code, respuesta.reason))
