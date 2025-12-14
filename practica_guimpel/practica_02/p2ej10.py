# Ejercicio 10. Escriba una función que reciba dos números como parámetros y
# devuelva cuántos múltiplos del primero hay que sean menores que el segundo.
# a) Implementarla utilizando un ciclo for, desde el primer número hasta el segundo.
# b) Implementarla utilizando un ciclo while, que multiplique el primer número hasta que sea
# mayor que el segundo.
# c) Comparar ambas implementaciones: ¿Cuál es más clara? ¿Cuál realiza menos operaciones?

def multiplos(a, b):
    """
    Docstring para multiplos
    Ejemplos:
    multiplos(5, 10) == 1 (el numero 2)
    multiplos(10, 100) == 9 (los nros 10, 20, 30 ..., 90)
    """
    contador = 0
    for i in range(a, b, a): # recorro todos los múltiplos de a menores que b. 
        contador = contador + 1
    return contador

def contar_multiplos(a, b):
    contador = 0
    valor = a
    while valor < b:
        contador = contador + 1
        valor = valor + a
    return contador


# Respondiendo al item C:
"""
Es claro que la versión con for con step, es la mas eficiente y clara.
En termino de operaciones, es la que realiza menos operaciones: una suma en cada iteracion.
en cambio, la version con while realiza 2 sumas en cada iteracion, ademas de requerir una variable más.
Sin embargo, ambas iteran la misma cantidad de veces.
"""