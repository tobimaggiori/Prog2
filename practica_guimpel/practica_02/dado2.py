# Simule n lanzamientos de dos dados, donde n es un valor que se debe pedir que se
# ingrese por teclado. Muestre cuántas veces los dados tuvieron el mismo resultado.
import random

def tirar_dado():
    return random.randint(1,6)

def tirar_dados(n):
    """
    tirar_dados: Natural -> None
    Dado un numero natural n, simula el lanzamiento de dos dados y imprime
    en pantalla las veces que los dados tuvieron el mismo resultado.
    """
    veces_iguales = 0
    for _ in range(n): # version mas limpia que for i in range(1, n+1).
        if tirar_dado() == tirar_dado():
            veces_iguales += 1
    print(f"Los dados tuvieron {veces_iguales} veces resultados iguales.")