import math
import random

print(pow(10,2))
print(math.sqrt(64))
#si necesito alguna operación matemática está math
#La librería random es para que sea aleatorio

print(random.randint(1,100))



def entero():
    print('este dato es un entero')
    return 10
def decimal():
    print('Este es un dato decimal')
    return 6.2
def frase():
    return 'esto es una frase'
print(entero())
print(decimal())
print(frase())

#Ejercicio 1
# Crear una funcion que pida dos numeros. Si el primero es mayor al segundo,
# el programa debe retornar el valor 1; si el segundo es mayor al primero,
# debe retornar -1; si ambos son iguales, debe retornar 0


def ej1(a,b):
    if a>b:
        return 1
    elif a<b:
        return -1
    else:
        return 0



print(ej1(2,2))

#Ejercicio 2
# Escribir una función que calcule el total de una factura tras aplicarle el IVA.
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar,
# y devolver el total de la factura.
# Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.


def total():
    valor=float(input("\nIngrese el valor del producto: "))
    iva=int(input("\nIngrese el valor del iva a aplicar: "))
    if iva!=0:
        if iva>0:
            total=(valor*(iva/100))+valor
            return "El valor total es: ",total
        else:
            return "ha ingresado un número negativo.\n"
    else:
        total=(valor*0.21)+valor
        return "el valor total del poducto es: ",total



print(total())
