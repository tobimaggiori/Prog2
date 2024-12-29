"""Ejercicio 1. Escribir una función que reciba una lista y un elemento, que:
1. devuelva la cantidad de apariciones del elemento recibido como parámetro, en la lista;
2. busque la primera coincidencia del elemento en la lista y devuelva su posición;
3. utilizando la función anterior, busque todos los elementos que coincidan con el recibido como
parámetro y devuelva una lista con las posiciones."""

def contar_apariciones(elemento, lista):
    """
    contar_apariciones : Any List -> Integer
    Dado un elemento y una lista, devuelve la cantidad
    de apariciones que el elemento aparece en la lista.
    Ejemplos:
    contar_apariciones("LCC",["LCC", "PM", "LM", "LCC"]) == 2
    contar_apariciones("LCC",["PM", "LM", "PF", "LF"]) == 0
    """
    contador = 0
    for i in lista:
        if i == elemento:
            contador = contador + 1
    return contador

def test_contar_apariciones():
    assert contar_apariciones("LCC",["LCC", "PM", "LM", "LCC"]) == 2
    assert contar_apariciones("LCC",["PM", "LM", "PF", "LF"]) == 0

def buscar_elemento(elemento, lista):
    """
    buscar_elemento : Any List -> Integer
    Dado un elemento y una lista, devuelve la
    posición de la aprimer aparición del elemento
    en la lista. Si no lo encuentra devuelve -1.
    Ejemplos:
    buscar_elemento(True,[False, True, False, True]) == 1
    buscar_elemento("LCC",["PM", "LM", "PF", "LF"]) == -1
    """
    rta = -1 # Si elemento no esta en la lista, devuelve -1.
    for i in range(0,len(lista)):
        if lista[i] == elemento and rta == -1:
            rta = i
    return rta

def test_buscar_elemento():
    assert buscar_elemento(True,[False, True, False, True]) == 1
    assert buscar_elemento("LCC",["PM", "LM", "PF", "LF"]) == -1

def buscar_en_lista(elemento, lista):
    """
    buscar_en_lista : Any List -> List(integer)
    Dado un elemento y una lista, devuelve una lista
    con cada posición que aparece el elemento en la lista.
    Ejemplos:
    buscar_en_lista(4,[0,1,2,3,4]) == [4]
    buscar_en_lista("LCC",["PM", "LM", "PF", "LF"]) == []
    buscar_en_lista(4,[4,4,4,4]) == [0, 1, 2, 3]
    """
    rta = [] # Si elemento no esta en la lista, devuelve []
    for i in range(0,len(lista)):
        if lista[i] == elemento:
            rta.append(i)
    return rta

def test_buscar_en_lista():
    assert buscar_en_lista(4,[0,1,2,3,4]) == [4]
    assert buscar_en_lista("LCC",["PM", "LM", "PF", "LF"]) == []
    assert buscar_en_lista(4,[4,4,4,4]) == [0, 1, 2, 3]
