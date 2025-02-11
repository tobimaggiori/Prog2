# Ejercicio 7. Diseñar una implementación propia de la función abs, 
# que devuelva el valor absoluto de cualquier valor que reciba.

def absoluto(a):
    """
    absoluto: Float -> Float
    Dado un numero real devuelve su distancia al origen.
    Ejemplos:
        absoluto(-5) == 5
        absoluto(4) == 4
        absoluto(0) == 0
    """
    if a <= 0:
        absol = a * -1
    else:
        absol = a
    return absol

def test_absoluto():
    absoluto(-5) == 5
    absoluto(4) == 4
    absoluto(0) == 0

def main():
    print("Programa para calcular el valor absoluto de un numero.")
    a = float(input("Ingresá un numero: "))
    print(f"El valor absoluto de {a} es {absoluto(a)}")

if __name__ == '__main__':
    main()