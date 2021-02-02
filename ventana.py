from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from insert import insert_datos
from kivy.clock import Clock
from kivy.uix.popup import Popup
import random
from update_puntaje import update_puntaje
from select import select_lista


class Principal_Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.contador_tiempo = 10
        self.contador_racha = 0

    def Mostrar(self):
        self.usu = str(self.ids.usuario.text)
        self.ids.mostrar_usuario.text = self.usu
    def Registrar(self):
        insert_datos(self.usu, 0)

    def Tiempo(self):
        Clock.schedule_interval(self.Contador,1)

    def Contador(self,dt):
        self.contador_tiempo -= 1
        self.ids.contador.text = str(self.contador_tiempo)
        if self.contador_tiempo == 0:
            Pop(self).open()
            Pop(self).llenar()
            return False
        """try:
            if self.a + self.b != int(self.ids.respuesta.text):
                #Pop(self).open()
                return False
        except:
            pass"""

    def Nueva(self):
        
        if self.a + self.b == int(self.ids.respuesta.text):
            self.contador_racha += 1
            self.ids.racha.text = str(self.contador_racha)
            self.contador_tiempo = 10
        elif self.a + self.b != int(self.ids.respuesta.text):
            
            Pop(self).open()
            Pop(self).llenar()
        self.ids.respuesta.text = ''

    def Generar_Numeros(self):
        self.a = random.randint(10,20)
        self.ids.numeroa.text = str(self.a)
        self.b = random.randint(15,25)
        self.ids.numerob.text = str(self.b)


class Pop(Popup):
    def __init__(self,As):
        super().__init__()
        self.As = As
        self.llenar()
        a = select_lista()
        nombres = []
        puntajes = []
        for i in range(len(a)):
            nombres.append(a[i][0])
            puntajes.append(a[i][1])
        try:
            self.ids.lblu1.text = str(nombres[0])
            self.ids.lblp1.text = str(puntajes[0])
            self.ids.lblu2.text = str(nombres[1])
            self.ids.lblp2.text = str(puntajes[1])
            self.ids.lblu3.text = str(nombres[2])
            self.ids.lblp3.text = str(puntajes[2])
        except:
            pass
        print(nombres)
        print(puntajes)
        
    def llenar(self):
        nombre_usuario = self.As.ids.usuario.text
        puntaje = self.As.ids.racha.text
        self.ids.labelnombre.text = nombre_usuario
        self.ids.labelpuntaje.text = puntaje
        update_puntaje(nombre_usuario,puntaje)




class PRUEBA(App):
    title = 'VENTANA PRINCIPAL'

    def build(self):
        sm = ScreenManager()
        sm.add_widget(Principal_Screen(name='principal'))

        return sm

if __name__ == '__main__':
    PRUEBA().run()