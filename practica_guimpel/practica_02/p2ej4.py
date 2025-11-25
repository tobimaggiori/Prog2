# Ejercicio 4. Escriba una función que tome una cantidad m de valores que serán ingresados
# por el usuario y, a medida que se ingresa cada número, muestre el factorial del mismo. El valor
# de m es ingresado inicialmente por el usuario.

# Interpretacion de la consigna como UNA (sola) funcion.
def factorial():
    m = int(input("Ingresá la cantidad de numeros a calcular su factorial: "))
    for x in range(m):
        numero = int(input(f"Ingresá el {x+1} numero a calcular su factorial: "))
        resultado = 1
        for i in range(1, numero+1):
            resultado = resultado * i
        print(f"El factorial de {numero} es {resultado}")

""" Funcion sola de calculo de factorial:
def factorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado = resultado * i
    return resultado
"""
factorial()