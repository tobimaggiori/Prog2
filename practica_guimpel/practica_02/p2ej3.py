# Ejercicio 3. Modifique el programa anterior para que
# pueda generar fichas de un juego que puede tener números de 0 a n.

"""
Representación de datos:
Una ficha es [a, b] donde a y b son enteros positivos y
a <= b, pues [a, b] = [b, a] para todo a y b. 
Ficha es List(Number).
"""

def crear_fichas(n):
    """
    n: valor máximo que puede tener una ficha.
    crear_fichas: Number -> List(Ficha)
    Dado el valor n crea una lista de Fichas, la cantidad de Fichas
    a crear es: 1 + 2 + 3 ... + n + (n+1). 
    Por ejemplo, para n = 6 creará 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28 fichas.
    Y la lista, por extensión sería: [ [0, 0], [0, 1], [0, 2], ..., [6, 6] ]
    """
    fichas = [[i, j] for i in range(n+1) for j in range(i, n+1)] # Def. por comprension.
    return fichas

def test_crear_fichas():
    assert len(crear_fichas(6)) == 28
    assert len(crear_fichas(7)) == 36
    assert len(crear_fichas(10)) == 66

"""
La definición de la funcion crear_fichas_2 y la siguiente, son equivalentes:

def crear_fichas_2(n):
    for i in range(n+1):
        for j in range(i, n+1):
            [i, j]

La definición por comprensión permite hacer lo mismo en menos código, su costo es, quizas,
que es menos legible.
"""
