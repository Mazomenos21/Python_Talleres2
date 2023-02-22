'''Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio;
luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro.
Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes.
Por último, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno
'''

class fabrica():
    def __init__(self,modelo,llantas,color,precio):
        self.modelo=modelo
        self.llantas=llantas
        self.color=color
        self.precio=precio
class moto(fabrica):
    def datos(self):
        print("El modelo de la moto es: ",self.modelo)
        print("La cantidad de llantas es: ",self.llantas)
        print("El color de la moto es: ",self.color)
        print("El precio de la moto es: ",self.precio)

class carro(fabrica):
    def datos(self):
        print("El modelo de la carro es: ",self.modelo)
        print("La cantidad de llantas es: ",self.llantas)
        print("El color del carro es: ",self.color)
        print("El precio del carro es: ",self.precio)


moto1=moto("Pulsar 200",2,"Azul",11500000)
carro1=carro("Renault",4,"Blanco",72000000)
moto1.datos()
carro1.datos()





