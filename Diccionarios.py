"""En el siguiente diccionario se encuentran capitales de los paises en el mundo,
 debes realizar un programa que pida un pais al usuario, y muestre la capital de ese pais,
 en dado caso el pais no este en el diccionario,
 se debe mostrar un mensaje diciendo que ese pais no se encuentra."""

dic1 = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras",
        "Nicaragua": "Managua",
        "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires",
        "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

op = input("Ingrese el país que desea conocer la capital: ")

if op.capitalize() in dic1 :
    print("La capital del país es: ", dic1[op.capitalize()])
else:
    print("No existe ese país en el diccionario.")


#Con el siguiente diccionario, debes crear un programa que pregunte al usuario por un número;
# el programa debe imprimir el jugador al que hace referencia ese número

dic2={

    1 : "Casillas", 15 : "Ramos",

    3 : "Pique", 5 : "Puyol",

    11 : "Capdevila", 14 : "Xabi Alonso",

    16 : "Busquets", 8 : "Xavi Hernandez",

    18 : "Pedrito", 6 : "Iniesta",

    7 : "Villa"

}


op1=int(input("Ingrese el número del jugador: "))

if op1 in dic2:
    print("El jugador es: ",dic2[op1])
else:
    print("No se ha encontrado el jugador.")
