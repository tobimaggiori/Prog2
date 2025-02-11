def contar_l(string, l, contar=0):
    """
    contar_a : String String -> Natural
    Dado un String y un caracter devuelve cuantas veces aparece
    el caracter en el String sin distinguir entre mayus/min.
    Ejemplos:
    contar_l("Hola", "L") == 1
    contar_l("Mundo!", "!") == 1
    contar_l("LCC", "e") == 0
    """
    minus = string.lower()
    char = l.lower()
    for x in range(len(string)):
        if minus[x] == char:
            contar = contar + 1
    return contar

def test_contar_l():
    assert contar_l("Hola", "L") == 1
    assert contar_l("Mundo!", "!") == 1
    assert contar_l("LCC", "e") == 0
    
def contarVocales(string):
    """
    contarVocales : String -> Tuple(Nat, Nat, Nat, Nat, Nat)
    Dado un String devuelve una tupla con la cantidad de vocales
    que este tiene en el orden a e i o u.
    Ejemplos:
    contarVocales("aeiou") == (1 , 1, 1, 1, 1)
    contarVocales("e") == (0, 1, 0, 0, 0)
    contarVocales("u") == (0, 0, 0, 0, 1)
    """
    for i in ["a","e","i","o","u"]:
        rta = contar_l(string, i)
        if i == "a":
            cuantas_a = rta
        elif i == "e":
            cuantas_e = rta
        elif i == "i":
            cuantas_i = rta
        elif i == "o":
            cuantas_o = rta
        else:
            cuantas_u = rta
    return cuantas_a,cuantas_e,cuantas_i,cuantas_o,cuantas_u

def test_contarVocales():
    assert contarVocales("aeiou") == (1 , 1, 1, 1, 1)
    assert contarVocales("e") == (0, 1, 0, 0, 0)
    assert contarVocales("u") == (0, 0, 0, 0, 1)

def main():
    print("Programa para calcular la cantidad de vocales de un String.")
    entrada = input("Ingrese el string del cual desea contar sus vocales: ")
    vocales = contarVocales(entrada)
    print(f"Su string tiene {vocales[0]} 'a', {vocales[1]} 'e', {vocales[2]} 'i', {vocales[3]} 'o', {vocales[1]} 'u'.")

if __name__ == '__main__':
    main()