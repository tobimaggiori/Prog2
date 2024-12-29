def contarLetras(string, result=0):
    longitud = 0
    """
    contarLetras: String Natural -> Natural
    Cuenta la longitud de la primer palabra de un string
    de palabras separadas por un espacio.
    Ejemplos:
    contarLetras("Tierra Sol Luna") == 6
    contarLetras("Sol Luna Tierra") == 3
    contarLetras(" LCC ") == 0
    """
    if string == "":
        return result
    else:
        if string[0] == " ":
            return result
        else:
            return contarLetras(string[1:], result+1)

def test_contarLetras():
    assert contarLetras("Tierra Sol Luna") == 6
    assert contarLetras("Sol Luna Tierra") == 3
    assert contarLetras(" LCC ") == 0

def mayoresDeCinco(string, result=0):
    """
    mayoresDeCinco : String Natural -> Natural
    Devuelve la cantidad de palabras de longitud mayor a 5 letras
    que tenga un string de palabras separadas por un espacio.
    Ejemplos:
    mayoresDeCinco("Sol Tierra Magia Computacion") == 2
    mayoresDeCinco("Sol Luna Luz LCC") == 0
    mayoresDeCinco("") == 0
    """
    if string == "":
        return result
    else:
        if contarLetras(string) > 5:
            return mayoresDeCinco(string[contarLetras(string)+1:], result+1)
        else:
            return mayoresDeCinco(string[contarLetras(string)+1:], result)

def test_mayoresDeCinco():
    assert mayoresDeCinco("Sol Tierra Magia Computacion") == 2
    assert mayoresDeCinco("Sol Luna Luz LCC") == 0
    assert mayoresDeCinco("") == 0

