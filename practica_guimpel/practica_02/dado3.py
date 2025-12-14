# Simule n lanzamientos de un dado en un juego con las siguientes reglas: si sale 6 gana
# 4 pesos; si sale 3 gana 1 dólar; si sale 1 sigue jugando y si sale 2, 4 o 5 pierde 2 pesos.
# Muestre los valores que salen y el resultado final del juego.

import random

def tirar_dado():
    return random.randint(1,6)

"""
A continuacion presento dos soluciones, una con while y otra con for.
Si bien el codigo de ambas es muy similar, es más adecuado, para esta consigna
el uso de for, ya que:
- No modifica n
- Usa la estructura de control correcta para un conteo fijo
- El control del ciclo está separado de la lógica del juego
"""

def resultado_tirada(dado, pesos, dolares):
    mensaje = ""
    if dado in {2,4,5}:
        pesos -= 2
        mensaje = f"Salió el {dado} ¡Perdiste 2 pesos!"
    elif dado == 6:
        pesos += 4
        mensaje = "Salió el 6 ¡Ganaste 4 pesos!"
    elif dado == 3:
        dolares += 1
        mensaje = "Salió el 3 ¡Ganaste 1 dolar!"
    else:
        mensaje = "Salió el 1 ¡Seguis jugando!"
    return pesos, dolares, mensaje

def test_resultado_tirada():
    assert resultado_tirada(2, 10, 0) == (8, 0, "Salió el 2 ¡Perdiste 2 pesos!")
    assert resultado_tirada(6, 0, 0) == (4, 0, "Salió el 6 ¡Ganaste 4 pesos!")
    assert resultado_tirada(3, 0, 5) == (0, 6, "Salió el 3 ¡Ganaste 1 dolar!")
    assert resultado_tirada(1, 7, 2) == (7, 2, "Salió el 1 ¡Seguis jugando!")

def jugar(n):
    dolares = 0
    pesos = 0
    for i in range(n-1, -1, -1):
        dado = tirar_dado()
        pesos, dolares, mensaje = resultado_tirada(dado, pesos, dolares)
        print(mensaje, f"Quedan {i} tiradas.")
    print(f"¡Fin de las tiradas! Obtuviste {pesos} pesos y {dolares} dolares.")

def main():
    print("Bienvenido al juego.")
    n = int(input("Cuantas tiradas de dados queres hacer?: "))
    print("¡Vamos a jugar!")
    jugar(n)

if __name__ == '__main__':
    main()

# La siguiente version no separa la logica de la interactividad.
""" def jugarr(n):
    dolares = 0
    pesos = 0
    for i in range(n-1, -1, -1):
        dadotirado = tirar_dado()
        if dadotirado in {2, 4, 5}:
            pesos = pesos - 2
            print(f"Salió el {dadotirado} ¡Perdiste 2 pesos! quedan {i} tiradas más.")
        elif dadotirado == 6:
            pesos = pesos + 4
            print(f"Salió el 6 ¡Ganaste 4 pesos! quedan {i} tiradas más.")
        elif dadotirado == 3:
            dolares = dolares + 1
            print(f"Salió el 3 ¡Ganaste 1 dolar! quedan {i} tiradas más.")
        else:
            print(f"Salió el 1 ¡Seguis jugando! quedan {i} tiradas más.")
    print(f"¡Fin de las tiradas! Obtuviste {pesos} pesos y {dolares} dolares.")
"""
# Version con while, que tampoco separa logica de interactividad:
""" def jugar_while(n):
    dolares = 0
    pesos = 0
    while n != 0:
        dadotirado = tirar_dado()
        n = n - 1
        if dadotirado in {2, 4, 5}:
            pesos = pesos - 2
            print(f"Salió el {dadotirado} ¡Perdiste 2 pesos! quedan {n} tiradas más.")
        elif dadotirado == 6:
            pesos = pesos + 4
            print(f"Salió el 6 ¡Ganaste 4 pesos! quedan {n} tiradas más.")
        elif dadotirado == 3:
            dolares = dolares + 1
            print(f"Salió el 3 ¡Ganaste 1 dolar! quedan {n} tiradas más.")
        else:
            print(f"Salió el 1 ¡Seguis jugando! quedan {n} tiradas más.")
    print(f"¡Fin de las tiradas! Obtuviste {pesos} pesos y {dolares} dolares.")
"""




