# Versión del ejercicio 6 usando la ecuación presentada como nota.

def funcion(n, var = 0):
    for x in range(1, n+1):
        var = (x*(x+1)) / 2
        print(var)

print(funcion(5))


"""
Respondiendo a ¿Qué versión realiza más operaciones?:
Entre esta version y la siguiente:

def triangular(n):
    suma = 0
    for x in range(1, n+1):
        suma = suma + x
        print(f'{x} - {suma}')

Esta funcion va a realizar UNA SUMA en cada iteracion. Por ende, va a realizar n operaciones.

La funcion con formula realiza TRES OPERACIONES en cada iteracion. Por ende, va a realizar 3n operaciones.

Si hablamos de iteraciones, ambas realizan la misma cantidad de iteraciones: n iteraciones.

La version más eficiente: versión sin formula.
"""
