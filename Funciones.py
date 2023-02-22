'''
Crear un programa que tenga una lista,
luego crear una funcion con la cual se van a pedir numeros al usuario para agregar a la lista.
Debes crear una segunda funcion en donde se ordenen los numeros pares e impares dentro de dos listas nuevas'''

lis=[1,2,3]

def primero():
    print("La lista es: ", lis)

    sw = False
    while sw == False:
        num = int(input("¿Desea adicionar algo a las lista?"
                        "1.Si."
                        "2.No.\n"))
        if num == 1:
            adicionar = int(input("Ingrese el número a adicionar: "))
            lista(lis, adicionar)
        elif num == 2:
            print("Gracias por utilizar el método de insertar. ")
            sw = True
        else:
            print("Ha ingresado un número incorrecto. ")

    print("La lista sin ordenar es: ", lis)

    print("La lista ordenada es: ", ordenar(lis))

    print(separar(lis))


def lista(lista1,adicion):
    lista1.append(adicion)

def ordenar(lista):
    lista.sort()
    return lista

def separar(lista):
    l=len(lista)
    lista_par=[]
    lista_impar=[]
    for i in range(l):
        if lista[i]%2==0:
            lista_par.append(lista[i])
        else:
            lista_impar.append(lista[i])
    print("La lista par es: ", lista_par)
    print("La lista impar es: ", lista_impar)

def factorial(num):
    # Crear una lista de números del 1 al 10
    numbers = list(range(1, num))

    # Recorrer la lista en reversa utilizando reversed()
    for number in reversed(numbers):
        print(number)  # imprime los números del 10 al 1


def segundo():
    '''Escribir una función que reciba un número entero positivo y devuelva su factorial.'''
    number=int(input("Ingrese el número que desea saber el factorial: "))
    factorial(number)




op=int(input("Ingrese el ejercicio: "))

if op==1:
    primero()
else:
    segundo()






