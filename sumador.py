from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen


class Sumador(Screen):
    numero1 = StringProperty()
    numero2 = StringProperty()
    resultado = StringProperty()

    def sumar(self):
        try:
            numero1Entero = int(self.numero1)
            numero2Entero = int(self.numero2)
        except:
            self.resultado = 'DEBE INGRESAR SOLO NÚMEROS'
            return

        resultadoEntero = numero1Entero + numero2Entero
        self.resultado = str(resultadoEntero)

    def irAFactorial(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'factorial'
