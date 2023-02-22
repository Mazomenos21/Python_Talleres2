"""Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar de ese numero"""

num1=int(input("Ingrese el número que desea saber las tablas de multiplicar: "))
i=1

while i<=10:
    print(num1,"x {}".format(i)," = ",i*num1)
    i+=1


#Escribir un programa que pregunte al usuario su edad
# y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

anio=int(input("Ingrese el año de nacimiento: "))
edad=int(input("Ingrese la edad que tiene: "))
j=0

while j<=edad:
    print("En {} cumplió: ".format(anio+j),j," años.")
    j+=1