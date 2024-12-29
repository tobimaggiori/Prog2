def primeros_caracteres(cadena, x = 2):
    """
    primeros_caracteres: String Number -> String
    Dada una cadena de caracteres y un numero x, devuelve
    los primeros x caracteres de la cadena dada. 
    * De no darse un numero, dara los primeros 2 caracteres de la cadena.

    Ejemplos:
    primeros_caracteres("Hola") == "Ho"
    primeros_caracteres("Hola", 3) == "Hol"
    primeros_caracteres("") == ""
    """
    return cadena[0:x]

def test_primeros_caracteres():
    assert primeros_caracteres("Hola") == "Ho"
    assert primeros_caracteres("Hola", 3) == "Hol"
    assert primeros_caracteres("") == ""

def ultimos_caracteres(cadena, z = 3):
    """
    ultimosZcaracteres : String Number -> String
    Dada una cadena devuelve sus últimos z caracteres.
    Ejemplos: si z = 3, entonces:
    ultimosZcaracteres("Hola FCEIA") == "EIA"
    ultimosZcaracteres("") == ""
    ultImosZcaracteres("Sol") == "Sol"
    """
    return cadena[len(cadena)-z:len(cadena)]

def test_ultimos_caracteres():
    assert  ultimos_caracteres("Hola FCEIA") == "EIA"
    assert  ultimos_caracteres("") == ""
    assert  ultimos_caracteres("Sol") == "Sol"

def imprimirCadaDos(cadena):
    """
    imprimirCadaDos : String -> String

    Dado un string no vacio lo devuelve cada dos caracteres,
    si el string es vacio lo devuelve sin modificar.

    Ejemplos:
    imprimirCadaDos("recta") == "rca"
    imprimirCadaDos("") == ""
    imprimirCadaDos("Pi") == "P"
    """
    if cadena == "":
        return "" # si cadena es un string vacio.
    else:
        return cadena[0:1] + imprimirCadaDos(cadena[2:len(cadena)]) # si cadena no es un string vacio.

def test_imprimirCadaDos():
    assert imprimirCadaDos("recta") == "rca"
    assert imprimirCadaDos("") == ""
    assert imprimirCadaDos("Pi") == "P"

def invertir_str(string):
    """
    invertir_str : String -> String
    Dado un string devuelve el resultado de invertirlo.
    Ejemplos:
    invertir_str("hola mundo!") == "!odnum aloh"
    invertir_str("") == ""
    invertir_str("4202") == "2024"
    """
    if string == "":
        return ""
    else:
        return string[-1] + invertir_str(string[:-1])

def test_invertir_str():
    assert invertir_str("hola mundo!") == "!odnum aloh"
    assert invertir_str("") == ""
    assert invertir_str("4202") == "2024"

def doble_sentido(string):
    """
    doble_sentido : String -> String
    Devuelve el string dado concatenado con el resultado de invertirlo.
    Ejemplo:
    doble_sentido("reflejo") == "reflejoojelfer"
    """
    if string == "":
        return ""
    else:
        return string + invertir_str(string)

def test_doble_sentido():
    assert doble_sentido("reflejo") == "reflejoojelfer"