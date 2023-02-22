''' Ejercicio 1
Crear un programa que tenga dos funciones,
una que contenga el area de un cuadrado con argumentos de base y altura;
y la otra el area de un circulo con argumento de radio'''
import math
def cuadrado(base,altura):
    area=base*altura
    return "El área del cuadrado es: ",area

def circulo(radio):
    areaCirculo=3.1*pow(radio,2)
    return "El área del circulo es: ",areaCirculo


print(cuadrado(3,4))
print(circulo(4))


#Ejercicio 2
# Escribir una función que reciba una muestra de números en una lista y devuelva su medida.

def lis(*tupla):
    print(len(tupla))


lis(2,3,4,10,20)