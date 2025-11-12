# Ejercicio 5. Escriba un programa que calcule e imprima el resultado de la suma de los
# primeros n  números naturales usando una función recursiva.

def sumar_primeros(n=50, suma=0):
    ''' 
    Devuelve la suma de los primeros n numeros naturales.
    sumar_primeros_n: Int -> Int
    '''
    if n == 0: # Notar que esta condicion tiene un llamado recursivo menos que n < 0. 
        return suma
    return sumar_primeros(n-1, suma+n) # Si aca no hay un return devuelve None.

# Si una función no tiene return explícito, Python devuelve automáticamente None.
# Pensemos la recursividad sin el return de la linea 11. Para n = 4.
# sumar_primeros(4)
#   == sumar_primeros(4-1, 0+4) == sumar_primeros(3, 4) -> Tiene return? -> None
#   == sumar_primeros(3-1, 4+3) == sumar_primeros(2, 7) -> Tiene return? -> None
#   == sumar_primeros(2-1, 7+2) == sumar_primeros(1, 9) -> Tiene return? -> None
#   == sumar_primeros(1-1, 9+1) == sumar_primeros(0, 10) -> Tiene return? -> 10
# _______________________________________________________________________________________________________
# Ahora, pensemos en la recursion con la presencia del return en la linea 11:
#   == sumar_primeros(4-1, 0+4) == sumar_primeros(3, 4) -> Tiene algo qué devolver? -> Sí, otra funcion.
#   == sumar_primeros(3-1, 4+3) == sumar_primeros(2, 7) -> Tiene algo qué devolver? -> Sí, otra funcion.
#   == sumar_primeros(2-1, 7+2) == sumar_primeros(1, 9) -> Tiene algo qué devolver? -> Sí, otra funcion.
#   == sumar_primeros(1-1, 9+1) == sumar_primeros(0, 10) -> Tiene algo qué devolver? -> 10

def test_sumar_primeros_n():
    sumar_primeros(50) == 1275

def main():
    n = int(input("Ingrese un natural: "))
    print("La suma de los primeros", n, "naturales es:", sumar_primeros(n, 0))

if __name__ == '__main__':
    main()