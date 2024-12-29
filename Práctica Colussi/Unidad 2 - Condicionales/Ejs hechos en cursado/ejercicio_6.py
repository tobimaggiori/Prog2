# Ejercicio 6. Diseñar tres funciones que resuelvan los siguientes problemas:
# a) Dado un número entero n, indicar si es par o no.
# b) Dado un número entero n, indicar si es múltiplo de tres o no.
# c) Dado un número entero n, y un factor f indicar si es múltiplo de f o no.

# ---------------------------------------------- Item a) ------------------------------------------
def es_par(num):
    """
    es_par: Number -> String
        entrada: Integer
        mensaje: String
    
    Dado un numero entero devuelve un mensaje
    indicando si el mismo es par o no.

    Ejemplos:
    es_par(5) = "El número no es par."
    es_par(-4) = "El número es par."
    es_par(0) = "El número es par."
    """
    if num % 2 == 0:
        mensaje = "El número es par."
    else:
        mensaje = "El número no es par."
    return mensaje

def test_es_par():
    assert es_par(5) == "El número no es par."
    assert es_par(-4) == "El número es par."
    assert es_par(0) == "El número es par."
    
# ---------------------------------------------- Item b) ------------------------------------------
def multiplo_de_tres(num):
    """
    multiplo_de_tres: Integer -> String
    entrada: Numero entero
    mensaje: String

    Dado un numero devuelve un String
    indicando si es o no multiplo de tres.
    
    Ejemplos:
    multiplo_de_tres(6) == "6 es multiplo de 3."
    multiplo_de_tres(7) == "7 no es multiplo de 3."
    """
    if ((num/3) - int(num/3) == 0):
        mensaje = f"{num} es multiplo de 3."
    else:
        mensaje = f"{num} no es multiplo de 3."
    return mensaje

def test_multiplo_de_tres():
    multiplo_de_tres(6) == "6 es multiplo de 3."
    multiplo_de_tres(7) == "7 no es multiplo de 3."
    
# ---------------------------------------------- Item c) ------------------------------------------
def n_esMultiploDe_f(n, f):
    """
    n_esMultiploDe_f: Integer Integer -> String
    Entradas:
        n (Integer)
        f (Integer)
    Devuelve: String que indica si n es o no un multiplo de f.

    Dado un número entero n, y un factor f devuelve
    un mensaje indicando si es múltiplo de f o no.
    Si f es = 0, devuelve "Ningun numero es multiplo de cero."

    Ejemplos:
    n_esMultiploDe_f(6, 3): "6 es multiplo de 3."
    n_esMultiploDe_f(4, 0): "Ningun numero es multiplo de cero."
    """
    if f == 0:
        mensaje = "Ningun numero es multiplo de cero."
    else:
        if ((n/f) - int(n/f) == 0):
            mensaje = f"{n} es multiplo de {f}."
        else:
            mensaje = f"{n} no es multiplo de {f}."
    return mensaje

def test_n_esMultiploDe_f():
    n_esMultiploDe_f(6, 3) == "6 es multiplo de 3."
    n_esMultiploDe_f(4, 0) == "Ningun numero es multiplo de cero."

# ---------------------------------------------- main ---------------------------------------------
def main():
    num = int(input("Ingrese un numero entero para saber si es o no un numero par: "))
    print(es_par(num))
    
    num2 = int(input("Ingrese un numero entero para saber si es o no un multiplo de 3: "))
    print(multiplo_de_tres(num2))
    
    print("Programa para calcular si un numero entero es multiplo de otro.")
    n = int(input("Ingrese un numero entero: "))
    f = int(input("Ingrese otro numero entero: "))
    print(n_esMultiploDe_f(n, f))
    
if __name__ == '__main__':
    main()