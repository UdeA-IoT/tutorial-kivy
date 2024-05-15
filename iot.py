from _thread import start_new_thread

from kivy.clock import mainthread
from kivy.properties import BooleanProperty, StringProperty, NumericProperty
from kivy.uix.screenmanager import Screen

from external_comm import UbidotsPublisher
from internal_comm import Listener, Publisher


class IoT(Screen):
    estadoLuz = BooleanProperty(False)
    imagen_luz = StringProperty('light_off.png')
    estado_termometro = NumericProperty(0.0)

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
            UbidotsPublisher.send_message('{variable}', '1')
        else:
            print('cambia a off')
            self.imagen_luz = 'light_off.png'
            UbidotsPublisher.send_message('{variable}', '0')



