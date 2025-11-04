# 1.1 Un problema dos soluciones
# Problema: pensar un numero, duplicarlo, sumarle seis, y dividirlo por dos, y restarle el numero elegido al comienzo. El numero que queda es siempre tres.

# Solucion 1:
def f1 (elegido):
    ''' Representamos el numero elegido mediante un numero float.
    # elegido: float
    # f1: float -> int
    # f1 recibe cualquier valor numerico y devuelve siempre el numero 3.
    # Ejemplos:
        # f1(3) = 3
        # f1(5) = 3
        # f1(19912) = 3
        # f1(3.14) = 3 '''
    return round(((elegido * 2) + 6) / 2 - elegido)  # Sin round para 3.14 da mal. 

def test_f1():
    # Prueba de f1
    assert f1(3) == 3
    assert f1(5) == 3
    assert f1(19912) == 3
    assert f1(3.14) == 3


# Solucion 2:
def f2 (elegido):
    ''' Representamos el numero elegido mediante un numero float.
    # elegido: float
    # f1: float -> int
    # f1 recibe cualquier valor numerico y devuelve siempre el numero 3.
    # Ejemplos:
        # f1(3) = 3
        # f1(5) = 3
        # f1(19912) = 3
        # f1(3.14) = 3 '''
    n = elegido * 2
    n =  n + 6
    n = n / 2
    n = n - elegido
    return n


# Ciclo for, ejemplo:def suma_cuadrados(n):
def cuadrado(n):
    return n*n

def suma_de_cuadrados(n, x=0):
    suma = 0
    for x in range(1, n+1):
        suma = suma + cuadrado(n)
    print(f'La suma de los primeros {n} cuadrados es {suma}.') # No es buena practica, sino un return, otra funcion imprime.


# Siempre debemos destacar:
# Organización y/o estructuración.
# División del problema en partes. (Modularidad)
# Visualización de una ejecución.