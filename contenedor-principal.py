from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from factorial import Factorial
from iot import IoT
from sumador import Sumador


class Contenedor(App):  # el archivo kv debe llamarse igual que esta clase
    sm = ScreenManager()

    def build(self):
        self.sm.add_widget(IoT(name='iot'))
        self.sm.add_widget(Sumador(name='sumador'))
        self.sm.add_widget(Factorial(name='factorial'))
        return self.sm


Contenedor().run()
