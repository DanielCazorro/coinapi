# Controladores que interactúan con el modelo y la vista
from tkinter import *

from .models import CriptoModel
from .views import CriptoView, CriptoViewTk


# Controlador principal para la aplicación de consola
class CriptoController:
    def __init__(self):
        self.modelo = CriptoModel()
        self.vista = CriptoView()

    def consultar(self):
        # Bucle para realizar consultas de cambio de moneda
        seguir = 's'
        while seguir.lower() == 's':
            ori, des = self.vista.pedir_monedas()

            self.modelo.origen = ori
            self.modelo.destino = des
            self.modelo.consultar_cambio()

            self.vista.mostrar_cambio(ori, des, self.modelo.cambio)

            seguir = ''
            while seguir.lower() not in ('s', 'n'):
                seguir = self.vista.quieres_seguir()



# Controlador para la interfaz gráfica de la aplicación
class CriptoControllerTk(Tk):
    def __init__(self):
        super().__init__()
        self.vista = CriptoViewTk(self, self.calcular_cambio)
        self.modelo = CriptoModel()

    def run(self):
        self.mainloop()

    def calcular_cambio(self):
        """
        Recoge los datos de la vista
        los pasa al modelo
        pide el cambio al modelo
        le pasa el resultado del cambio a la vista
        """
        self.modelo.origen = self.vista.moneda_origen()
        self.modelo.destino = self.vista.moneda_destino()
        self.modelo.consultar_cambio()

        self.vista.mostrar_cambio(self.modelo.cambio)
