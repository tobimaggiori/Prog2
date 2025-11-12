# Ejercicio 7. Escriba un programa que reciba un nombre y
# retorne el nombre pasado concatenado 2 veces. Es decir, 
# supongamos que la función se llama duplica, si hacemos duplica(”F ederico”)
# el resultado que deberíamos obtener sería: ”F edericoF ederico”.


def concatenar(s):
    """
    concatenar: String -> String
    Dado un String lo devuelve duplicado:
    entrada: "Tobi", salida: "TobiTobi"
    """
    return s * 2

def test_concatenar():
    concatenar("Tobi") == 'TobiTobi'

