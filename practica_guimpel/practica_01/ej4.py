# Ejercicio 4. Escriba un programa que calcule e imprima
# el resultado de la suma de los primeros 50 números
# naturales usando una función recursiva.

def sumar_primeros_n(n=50, suma=0):
    if n < 0:
        return(suma)
    sumar_primeros_n(n-1, suma+n)

def test_sumar_primeros_n():
    sumar_primeros_n(50) == 1275
 
