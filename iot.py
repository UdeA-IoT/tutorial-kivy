from _thread import start_new_thread

from kivy.clock import mainthread
from kivy.properties import BooleanProperty, StringProperty
from kivy.uix.screenmanager import Screen

from comm import Listener, Publisher


class IoT(Screen):
    estadoLuz = BooleanProperty(False)
    imagen_luz = StringProperty('light_off.png')

    def __init__(self, **kw):
        super().__init__(**kw)
        escuchador = Listener(self)
        try:
            start_new_thread(escuchador.start, ())
        except Exception as ex:
            print("Error: no se pudo iniciar el hilo. ex: {}".format(ex))


    def alternarLuz(self):
        Publisher.send_message('alternar_luz')


    @mainthread
    def procesarMensajeLuz(self, msg):
        print('recibido: {}'.format(msg))
        self.estadoLuz = not self.estadoLuz
        if self.estadoLuz:
            print('cambia a on')
            self.imagen_luz = 'light_on.png'
        else:
            print('cambia a off')
            self.imagen_luz = 'light_off.png'


