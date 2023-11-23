# Interacción con el usuario a través de la consola o la interfaz gráfica
from tkinter import StringVar, ttk

from . import MONEDAS

# Vista para la aplicación de consola
class CriptoView:
    def pedir_monedas(self):
        # Solicitar al usuario las monedas a intercambiar
        origen = input('¿Qué moneda quieres cambiar? ')
        destino = input('¿Qué moneda deseas obtener? ')

        return (origen, destino)

    def mostrar_cambio(self, origen, destino, cambio):
        # Mostrar el resultado del cambio al usuario
        print(f'Un {origen} vale lo mismo que {cambio:,.2f} {destino}')

    def quieres_seguir(self):
        # Preguntar al usuario si desea continuar consultando cambios
        seguir = input('¿Quieres consultar de nuevo? (S/N) ')
        return seguir

# Vista para la interfaz gráfica de la aplicación
class CriptoViewTk(ttk.Frame):
    def __init__(self, padre, accion):
        super().__init__(padre, width=400, height=400, padding=20)
        self.lo_que_hace_el_boton = accion
        self.grid()
        self.crear_controles()

    def crear_controles(self):
        # entrada moneda origen
        etiqueta_entrada = ttk.Label(self, text="Moneda origen")
        etiqueta_entrada.grid(row=0, column=0)

        self.origen = StringVar()
        combo_entrada = ttk.Combobox(
            self, values=MONEDAS, textvariable=self.origen)
        combo_entrada.grid(row=1, column=0)

        # entrada moneda destino
        etiqueta_destino = ttk.Label(self, text="Moneda destino")
        etiqueta_destino.grid(row=0, column=1)

        self.destino = StringVar()
        combo_destino = ttk.Combobox(
            self, values=MONEDAS, textvariable=self.destino)
        combo_destino.grid(row=1, column=1)

        # etiqueta para el resultado
        self.etiqueta_resultado = ttk.Label(self, text="0.0", padding=20)
        self.etiqueta_resultado.grid(row=2, column=0, columnspan=2)

        # botón para el cambio
        self.boton_calcular = ttk.Button(
            self, text="Calcular", command=self.lo_que_hace_el_boton)
        self.boton_calcular.grid(row=3, column=1)

    def moneda_origen(self):
        return self.origen.get()[:3]

    def moneda_destino(self):
        return self.destino.get()[:3]

    def mostrar_cambio(self, resultado):
        valor = "El valor actual es {:,.2f}".format(resultado)
        self.etiqueta_resultado.config(text=valor)
