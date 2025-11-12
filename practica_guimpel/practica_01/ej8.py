# Ejercicio 8. Escriba un programa que reciba un nombre y un número n,
# y retorne el nombre pasado concatenado n veces.

def concatenar(s, n):
    """
    concatenar: String -> String
    Dado un String lo devuelve concatenado n veces:
    concatenar("Tobi", 3), salida: "TobiTobiTobi"
    """
    return s * n

def test_concatenar():
    concatenar("Tobi", 3) == 'TobiTobi'