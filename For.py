"""Imprimir por pantalla los numeros del 1 al 10, luego,
pedir al usuario dos numeros y mostrar el rango de numeros entre ambas cifras"""

for i in range(1,11):
    print(i)

num1=int(input("Ingrese el primer número: "))
num2=int(input("Ingrese el segundo número: "))

for i in range(num1,num2+1):
    if (i%2)==0:
        print(i)
    else:
        continue

