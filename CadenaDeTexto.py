#\"  apply double quote to string
cadena="Esto Es Una Cadena De Texto"

print(cadena[:10])
# [0:size]   se trata un string como vector común y corriente


#.lower   convert lowercase to uppercase    (minuscula a mayuscula)
print(cadena.lower())

#.upper   convert  uppercase to lowercase   (mayúscula a minúscula)
print(cadena.upper())




ejercise="Te quiero solo como amigo"

# Imprima los dos primeros caracteres.
print(ejercise[:2])


# Imprima los tres últimos caracteres.
print(ejercise[-3:])

#Imprima dicha cadena cada dos caracteres. Ej.: Si la cadena fuera “recta” debería imprimir rca
print(ejercise[: :2])

#Dicha cadena en sentido inverso. Ej.: Si la cadena fuera hola mundo! debe imprimir !odnum aloh
print(ejercise[: :-1])



#Imprima la cadena en un sentido y en sentido inverso. Ej: Si la cadena es “reflejo” imprime reflejoojelfer.
print(ejercise + ejercise[: :-1])



ejercise2="separado"
remplazo=ejercise2.replace("",",")
print(remplazo)


