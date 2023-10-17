from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen


class Factorial(Screen):
    numeroIngresado = StringProperty()  # binding
    resultado = StringProperty()  # binding

    def calcularFactorial(self):
        try:
            numeroEntero = int(self.numeroIngresado)
        except:
            self.resultado = 'INGRESE SÓLO VALORES NUMÉRICOS'
            return
        factorial = 1
        for i in range(2, numeroEntero + 1):
            factorial *= i
        self.resultado = str(factorial)

    def irASumador(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'sumador'
