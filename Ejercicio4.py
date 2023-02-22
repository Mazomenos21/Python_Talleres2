'''Crear una clase llamada Marino(), con un metodo que sea hablar,
en donde muestre un mensaje que diga "Hola...". Luego,
crear una clase Pulpo() que herede Marino,
pero modificar el mensaje de hablar por "Soy un Pulpo". Por ultimo,
crear una clase Foca(), heredada de Marino,
pero que tenga un atributo nuevo llamado mensaje y que muestre ese mesjae como parametro'''

class marino():
    def hablar(self):
        print("Hola ")

class pulpo(marino):
    def hablar(self):
        print("soy un pulpo")

class foca(marino):
    def hablar(self,mensaje):
        self.mensaje=mensaje
        print(self.mensaje)

marino=marino()
marino.hablar()


pulpo=pulpo()
pulpo.hablar()

foca=foca()
foca.hablar("Hola,soy una foca")

