# ----------------------------------
# Programa que dado dos números
# imprime la suma, resta, división
# y multiplicación de ambos.
# Tobias Maggiori - Legajo: M-7137/4
# Catedra Programación II - LCC UNR.
# Rosario, 14 de marzo de 2024.
# ----------------------------------

def suma(a, b):
    """
    Signatura:
     resta: Number Number -> Number
    Proposito:
     Dado dos numeros a y b devuelve
     el reultado de operar a más b.
    Ejemplos:
     suma(10, 5) = 15
     suma(-5, 10) = 5
    """
    amasb = a + b
    return amasb

def test_suma():
    assert suma(10, 5) == 15
    assert suma(-5, 10) == 5

def resta(a, b):
    """
    Signatura:
     resta: Number Number -> Number
    Proposito:
     Dado dos numeros a y b devuelve
     el reultado de operar a menos b.
    Ejemplos:
     resta(10, 5) = 5
     resta(5, 10) = -5
    """
    amenosb = a - b
    return amenosb

def test_resta():
    assert resta(10, 5) == 5
    assert resta(5, 10) == -5

def division(a, b):
    """
    Signatura: 
     division: Number Number -> Number | String
    Proposito:
     Dados dos numeros a y b devuelve
     el resultado de operar a sobre b.
     Si b = 0 devuelve "No existe.".
    Ejemplos:
     division(10, 5) = 2
     division(5, 0) = "No existe."
    """
    if b == 0:
        return print("No existe.")
    else:
        asobreb = a / b
    return asobreb

def test_division():
    assert division(10, 5) == 2
    assert division(5, 0) == "No existe."

def multiplicacion(a, b):
    """
    Signatura:
     multiplicacion: Number Number -> Number
    Proposito:
     Dados dos numeros a y b devuelve
     el resultado de operar a por b.
    Ejemplos:
     multiplicacion(5, -3) = -15
     multiplicacion(3, 0) = 0 
    """
    aporb = a * b
    return aporb

def test_multiplicacion():
    assert multiplicacion(5, -3) == -15
    assert multiplicacion(3, 0) == 0

