'''Realizar un programa en el cual se declaren dos valores
enteros por teclado utilizando el método __init__.
Calcular después la suma, resta, multiplicación y división.
Utilizar un método para cada una e imprimir los resultados obtenidos.
Llamar a la clase Calculadora.
'''

class calculadora():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        return self.a+self.b
    def rest(self):
        return self.a-self.b
    def multi(self):
        return self.a * self.b
    def div(self):
        return self.a/self.b

ap=int(input("Ingrese el número A: "))
bp=int(input("Ingrese el número B: "))

resultado=calculadora(ap,bp)

print("El resultado de la suma es: ",resultado.sum())
print("El resultado de la resta es: ",resultado.rest())
print("El resultado de la multiplicación es: ",resultado.multi())
print("El resultado de la división es: ",resultado.div())





