
"""
Modelo <=> Controlador <=> Vista
Modelo </////> Vista (NUNCA hay comunicación entre el modelo y la vista directamente)
"""


class CriptoView:

    def __init__(self):
        pass

    def pedir_monedas(self):
        origen = input("¿Qué moneda quieres cambiar?")
        destino = input("¿Qué moneda deseas obtener?")
        pass

    def mostrar_cambio(self, origen, destino, cambio):
        print("Un {} vale como {:,.2f} {}".format(
            origen, cambio, destino))
        pass

    def quieres_seguir(self):
        seguir = input("¿Quieres cambiar algo más? (s/n)")
        return seguir.upper()
