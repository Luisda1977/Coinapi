from tkinter import Tk

from .models import CriptoModel
from .views import CriptoView, CriptoViewTk


class CriptoController:
    def __init__(self):
        # instancio la vista y el modelo
        self.modelo = CriptoModel()
        self.vista = CriptoView()

    def consultar(self):
        seguir = "S"
        while seguir.upper() == "S":
            desde, hasta = self.vista.pedir_monedas()
            self.modelo.moneda_origen = desde
            self.modelo.moneda_destino = hasta
            self.modelo.consultar_cambio()
            self.vista.mostrar_cambio(desde, hasta, self.modelo.cambio)

            seguir = ""
            while seguir.upper() not in ("S", "N"):
                seguir = self.vista.quieres_seguir()


class CriptoControllerTk(Tk):
    def __init__(self):
        super() .__init__()
        self.vista = CriptoViewTk(self)
        self.modelo = CriptoModel()

    def run(self):
        self.mainloop()
