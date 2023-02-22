import math
nombre=input("Digita tu nombre : ")
edad=int(input("Ingresa tu edad : "))
sexo=input("Digita tu sexo: ")
letra=input("Digite letra en mayúscula: ")
vocal=input("Digite vocal en minúscula: ")

print("Letra en minúscula ",letra.lower(),"\nVocal en mayúscula ",vocal.upper())
print("Te llamas: {}\nTu edad es: {}\nEres: {}".format(nombre,edad,sexo))

print("Ejercicio 1")

#fórmula del estudiante   ->   formula of student
a=int(input("Ingrese el numero a: "))
b=int(input("Ingrese el numero b: "))
c=int(input("ingrese el numero c: "))
formula1=0
formula2=0
if ((b**2)-(4*(a*c)))<0:
    print("No se puede sacar raíz de números negativos.")
else:
    formula1 = ((-b + math.sqrt((b**2) - (4 * a * c))) / (2 * a))
    formula2 = ((-b - math.sqrt((b**2) - (4 * a * c))) / (2 * a))
    print("La primera opción de la ecuación es: ", formula1)
    print("La segunda opción de la ecuación es: ", formula2)



#prom of course

p1=float(input("Ingrese la nota de la practica 1: "))
p2=float(input("Ingrese la nota de la practica 2: "))
p3=float(input("Ingrese la nota de la practica 3: "))
PP=(p1+p2+p3)/3
EP=float(input("Ingrese la nota del exámen parcial: "))
EF=float(input("ingrese la nota del exámen final: "))

prom=( PP + 2*EP + 3*EF ) / 6

print("El promedio del estudiante es: ",prom)