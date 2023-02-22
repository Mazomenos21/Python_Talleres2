"""En la siguiente lista,
debes hacer un programa que muestre los valores al usuario,
a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:

[20, 50, "Curso", 'Python', 3.14]"""

lista=[20, 50, "Curso", 'Python', 3.14]

print("La lista inicial es: ",lista)


num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
lista[0]=num1
lista[1]=num2

print("La lista final es: ",lista)


#"""Escribe una lista que tenga los números de 1 al 10.
#Luego, debes hacer que los datos que están en las posiciones 4, 7 y 9 sean multiplicados por 2
#; por último, mostrar la lista nueva con los nuevos datos

lista2=[1,2,3,4,5,6,7,8,9,10]
print("La lista de numeros sin modificar es: ",lista2)
lista2[3]*=2
lista2[6]=(lista2[6])*2
lista2[8]=(lista2[8])*2

print("La lista de numeros modificada es: ",lista2)
