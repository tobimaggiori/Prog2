#  Ejercicio 1 = Ejercicio 2 = Ejercicio 3:
def imprimir_pares(n, actual=0):
    """
    imprimir_pares : Natural Natural -> None
    Recibe un n y un m, naturales y devuelve los primeros
    n pares >= m. 
    """
    if n == 0:
        return
    else:
        print(actual)  # Imprime el número actual
        imprimir_pares(n-1, actual+2)  # Llama recursivamente para el siguiente número

# Llamar a la función para imprimir los primeros 25 números pares
# imprimir_pares(25, 10)
# ___________________________________________________________________

#  Ejercicio 4 = Ejercicio 5
def sumar_primeros(n, suma=0):
    """
    sumar_primeros : Natural -> None
    Dado un numero natural n, imprime la suma de
    los primeros n naturales (Considerando el 0).
    """
    if n==1:
        print(suma)
    else:
        suma = suma + (n-1)
        sumar_primeros(n-1, suma)
# ___________________________________________________________________

# Ejercicio 6:
def sumar_entre(n, m, suma=0):
    """
    sumar_entre: Natural Natural -> None
    Recibe dos naturales, n y m, e imprime la suma
    de los numeros mayores que n y menores que m.
    Ejemplo:
    sumar_entre(5, 10) -> 30
    """
    if n+1 == m:
        print(suma)
    else:
        suma = suma + (m-1)
        sumar_entre(n, (m-1), suma)

# sumar_entre(5, 10)
# ___________________________________________________________________

# Ejercicio 7:
def duplicar_cadena(s):
    return s + s

# Ejercico 8:
def nplicar_cadena(s, n):
    return s * n
# ___________________________________________________________________

