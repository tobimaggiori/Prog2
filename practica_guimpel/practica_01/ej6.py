# Ejercicio 6. Escriba un programa que calcule e imprima el resultado
# de la suma de los números naturales mayores que n
# y menores que m usando una función recursiva.

def sumar_mayores(n=0, m=0, suma=0):
    ''' 
    Devuelve la suma de los primeros n numeros naturales.
    sumar_primeros_n: Int -> Int
    Dado dos numeros naturales, n y m tal que n < m, devuelve la suma
    de los mayores que m y menores que n:
    sumar_mayores(5, 10) == 6 + 7 + 8 + 9 == 30
    '''
    m = m - 1 # Necesito que en el primer llamado a m se le reste 1, por la consigna.
    if n == m:
        return suma
    return sumar_mayores(n, m, suma+m) # Si aca no hay un return devuelve None.

def test_sumar_mayores():
    assert sumar_mayores(5, 10) == 30