"""
Ejercicio 2. Escribir una función que tome una lista de números que:
1. devuelva el valor máximo;
2. devuelva el valor mínimo;
3. devuelva una tupla con el valor máximo y mínimo.
4. devuelva una tupla que incluya el valor máximo y su posición;
5. devuelva una tupla que incluya el valor mínimo y su posición;
6. ¿qué sucede si hay mas de un máximo y un mínimo? -> Devuelve ultima posicion.
7. ¿qué sucede si los elementos son listas de caracteres? qsyo
"""

def maximo(lista):
    rta = lista[0]
    for i in lista:
        if i > rta:
            rta = i
    return rta

def minimo(lista):
    rta = lista[0]
    for i in lista:
        if i < rta:
            rta = i
    return rta

def tupMaxMin(lista):
    return (minimo(lista), maximo(lista))

def tupMaxpos(lista):
    rta_max = lista[0]
    rta_pos = 0
    for i in lista:
        if i > rta_max:
            rta_max = i
            rta_pos = rta_pos + 1
    return (rta_max, rta_pos)

def tupMinpos(lista):
    rta_min = lista[0]
    rta_pos = 0
    for i in lista:
        if i < rta_min:
            rta_min = i
            rta_pos = rta_pos + 1
    return (rta_min, rta_pos)


print(tupMinpos([-5,0,1,2,3,4,5,6,7,8,9,10]))