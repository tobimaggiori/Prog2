# Ejercicio 12. Escriba una función que reciba un número natural e imprima todos los números
# primos que hay menores o iguales que ese número. Para esto se pide que:
# a) Defina una función es_primo que toma un número natural y verifica si es un número primo.
# b) Resuelva el problema usando la función definida en el punto anterior.

"""
- Los numeros primos son únicamente naturales mayores a 1: Si 1 => n entonces n es compuesto.
- Teorema: si n es compuesto entonces EXISTE d tal que 1 < d < raizCuad(n) y d divide exactamente a n.
- El unico par primo es el 2 => si n>2 y n es par => n no es primo.
- Por el teorema probamos si n es compuesto probando si tiene divisores entre 1 y su raiz cuadrada.
- Si NO existe un d para n entonces n es compuesto => n es primo.

"""
def es_primo(n):
    """
    es_primo: Number -> Bool
    Recibe un número y devuelve True si es primo o False si no lo es.
    Ejemplos:
    entrada: 1, salida: False
    entrada: 2, salida: True
    entrada: 3.14, salida: False
    """
    es_primo = True   # Suponemos que n es primo.
    if n <= 1 or type(n) != int:
        es_primo = False # Si n es 1 o no es natural => no es primo.
    else:
        d = 2
        while d * d <= n and es_primo: # Por el teorema planteado: [d*d <= n] <=> d <= raiz^2(n)
            if n % d == 0:
                es_primo = False
            d = d + 1
    return es_primo

""" Pensando en la funcion es_primo
Si es n no es un numero natural o n es igual a 1, entonces devuelve False.
Si n es un natural diferente a 1, entonces ejecuta un ciclo while que:
- 1 iteracion: 2 * 2 <= n and True: con if comprueba si n / d es entero: 
si esto sucede entonces n es un numero compuesto por el teorema planteado.
Modifica la variable de retorno a False. Aumenta 1 a d.
Continua el while hasta que d * d sea mayor a n.
"""

def devolver_primos(n):
    """
    devolver_primos: 
    """
    for i in range(2, n+1):
        if es_primo(i):
            print(i)

def main():
    print("Este programa le permite saber todos los primos menores o iguales al natural que usted ingrese.")
    n = int(input("Ingresa un número natural: ")) #Incluimos al 0
    if n > 1:
        print(f"Los numeros primos menores o iguales a {n} son: ")
        devolver_primos(n)
    else:
        print(f"El número {n} no tiene primos menores o iguales a él.")

main()
