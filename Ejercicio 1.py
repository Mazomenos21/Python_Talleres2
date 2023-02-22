'''Realizar un programa que conste de una clase llamada Estudiante,
que tenga como atributos el nombre y la nota del alumno.
Definir los métodos para inicializar sus atributos,
imprimirlos y mostrar un mensaje con el resultado de la nota
y si ha aprobado o no.'''


class estudiante():
    def __init__(self,nombre,nota):
        self.nom=nombre
        self.nota=nota
    def imprimir(self):
        print("Nombre: {}\nNota: {}".format(self.nom,self.nota))
    def resultado(self):
        if self.nota>3:
            print("Has APROBADO.")
        else:
            print("Has REPROBADO.")

estudiante1=estudiante("Stiven",4.3)
estudiante1.imprimir()
estudiante1.resultado()


