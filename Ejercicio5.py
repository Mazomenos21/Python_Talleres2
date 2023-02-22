'''Crear un programa con tres clases Universidad,
con atributos nombre (Donde se almacena el nombre de la Universidad).
Otra llamada Carerra, con los atributos especialidad
(En donde me guarda la especialidad de un estudiante).
Una ultima llamada Estudiante, que tenga como atributos su nombre y edad.
El programa debe imprimir la especialidad, edad,
nombre y universidad de dicho estudiante con un objeto llamado persona.'''

class universidad():
    def __init__(self,nom):
        self.nom=nom


class carrera():
    def carrera(self,especialidad):
        self.especialidad=especialidad



class estudiante(universidad,carrera):
    def datos(self,nom,edad):
        self.nom=nom
        self.edad=edad
        print("El nombre de la universidad es: ", self.nom)
        print("La especialidad de la carrera es: ", self.especialidad)
        print("El nombre del estudiante es: ", self.nom)
        print("La edad de la persona es: ", self.edad)


persona=estudiante("Politécnico")
persona.carrera("Sistemas")
persona.datos("Stiven Mazo",20)