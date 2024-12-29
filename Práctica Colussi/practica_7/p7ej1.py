# Representacion de una Carta de bajara francesa:
# Carta es: (valor, palo)
# Donde valor puede ser cualquier elemento de la siguiente tupla:
# (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A')
# Y palo puede ser cualquier elemento de la siguiente tupla:
# ('corazones', 'diamantes', 'tréboles', 'picas')
# De no cumplise estas condiciones, el elemento no es una carta de baraja francesa.

def crear_carta(valor, palo):
    """
        crear_carta : Number|String String -> Carta
    Recibe un valor y un palo para crear una carta de baraja francesa. (documentacion lineas 1-7)
    Si los argumentos recibidos son válidos devuelve la tupla (valor, palo),
    de lo contrario, devuelve un mensaje indicando el error.
        Ejemplos:
    crear_carta(2, "corazones") == (2, "corazones")
    crear_carta(5, "diamantes") == (5, "diamantes")
    crear_carta(1, "picas") == "Valor inválido: 1. Los valores válidos son:
    (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A')"
    """
    valores_validos = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A')
    palos_validos = ('corazones', 'diamantes', 'tréboles', 'picas')

    if valor in valores_validos:
        if palo in palos_validos:
            retorno = (valor, palo)
        else:
             retorno = f"Palo inválido: {palo}. Los palos válidos son: {palos_validos}"
    else:
        retorno = f"Valor inválido: {valor}. Los valores válidos son: (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A')"
    return retorno

def test_crear_carta():
    assert crear_carta(2, "corazones") == (2, "corazones")
    assert crear_carta(5, "diamantes") == (5, "diamantes")
    assert crear_carta(1, "picas") == "Valor inválido: 1. Los valores válidos son: (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A')"

def es_poker(c1, c2, c3, c4, c5):
    """
    es_poker : Carta Carta Carta Carta Carta -> Boolean
    Dado 5 cartas devuelve True si la mano es Poker o False si no lo es.
    Ejemplos:
    es_poker((3, "corazones"), (3, "diamantes"), (3, "treboles"), (3, "picas"), (4, "picas")) == True
    es_poker((3, "corazones"), (3, "diamantes"), (7, "diamantes"), (3, "picas"), (4, "picas")) == False
    """
    valores = (c1[0], c2[0], c3[0], c4[0], c5[0]) #Tupla con solo los valores como elementos.
    rta = False
    for i in valores: # Iteramos los valores.
        contador = sum(1 for n in valores if n == i) # Sumar 1 cada vez que n == i (2 valores =)
        if (contador == 4): # Rta = True si contador == 4, else rta = False
            rta = True
    return rta

def test_es_poker():
    assert es_poker((3, "corazones"), (3, "diamantes"), (3, "treboles"), (3, "picas"), (4, "picas")) == True
    assert es_poker((3, "corazones"), (3, "diamantes"), (7, "diamantes"), (3, "picas"), (4, "picas")) == False
