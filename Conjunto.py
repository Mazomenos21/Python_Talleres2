"""Escribir una tupla con los meses del año, luego, pide al usuario un numero,
el que haya ingresado, es el mes que debe mostrar en la tupla"""
tupla1= "No existe","Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"

op=int(input("Ingrese el número del mes que desea saber: "))

if op==0 or op>12:
    print("El número que ha ingresado es incorrecto")
else:
    print("Es el mes: ",tupla1[op])



#Escribir una tupla que tenga las letras del alfabeto.
# Luego, debes pedir al usuario un número,
# el que haya ingresado, es la letra que debe
# imprimir el programa

tupla2="","a", "b", 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', \
       'u', 'v', 'w', 'x', 'y', 'z'

op2=int(input("Ingrese el numero de la letra que desea saber: "))

if op2==0 or op2>27:
    print("Ha ingresado un número incorrecto")
else:
    print("La letra que eligió fue: ",tupla2[op2])


