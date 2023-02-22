letra=input("Digite una letra: ")

if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u" or letra.upper()=="A" or letra.upper()=="E" or letra.upper()=="I" or letra.upper()=="O" or letra.upper()=="U":
    print("Es una vocal.\n")
else:
    print("No es una vocal\n")


num=int(input("Ingrese un numero: "))

if num<0:
    num=num*-1
    print("El valor absoluto del numero es: ",num)
else:
    print("El valor absoluto del numero es: ", num)

pal1=input("Ingrese palabra #1: ")
pal2=input("Ingrese palabra #2: ")

if pal1[-3:]==pal2[-3:]:
    print("Las palabras riman.")
elif pal1[-2:] == pal2[-2:]:
    print("Las palabras riman un poco.")
else: print("Las palabras no riman.")


A="ROJO"
B="VERDE"
C="AZUL"

op=input("Ingrese la opcion del candidato a votar:\n")

if op.upper()=="A":
    print("Ha votado por el partido "+A)
elif op.upper()=="B":
    print("Ha votado por el partido "+B)
elif op.upper()=="C":
    print("Ha votado por el partido "+C)
else:print("Ha ingresado una opción incorrecta.")