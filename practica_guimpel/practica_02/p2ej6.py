# Ejercicio 6. Escriba una función que reciba un número n
# como parámetro e imprima los primeros n números triangulares,
# junto con sus respectivos índices. El número triangular n se
# obtiene mediante la suma de los números naturales desde 1 hasta n.
# Por ejemplo, si se piden los primeros 5 numeros triangulares
# el programa debería imprimir:
# 1 - 1
# 2 - 3
# 3 - 6
# 4 - 10
# 5 - 15

""" Modelo recursivo de la funcion triangular.
def triangular_recursiva(n):
    if n > 0:
        n = n + triangular_recursiva(n-1)
    return n
"""

# Si no sale pensarla directamente en con for, pensala recursiva y luego llevala.
def triangular(n):
    """
    triangular_for: Number -> Number
    Recibe un numero n y devuelve su triangular: la suma de
    los numeros naturales desde 1 hasta n.
    Ejemplos:
    Entrada: 3, salida: 6
    Entrada: 5, salida: 15
    Entrada: 1, salida: 1
    """
    suma = 0
    for x in range(1, n+1):
        suma = suma + x
    return suma

def test_triangular():
    assert triangular(3) == 6
    assert triangular(5) == 15
    assert triangular(1) == 1

def main():
    n = int(input("Ingresa el número: "))
    for x in range(1, n+1):
        print(f'{x} - {triangular(x)}')
        # Fichate el triangular(x), pensalo!

"""
Se puede mejorar la eficiencia de este codigo: la funcion triangular calcula el triangular de todos los numeros hasta n
pero se la esta utilizando para devolver el triangular solo de n, podria devolver una lista con todos los triangulares.
Luego imprimirlos en el main.
"""

if __name__ == '__main__':
    main()