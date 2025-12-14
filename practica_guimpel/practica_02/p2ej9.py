# Ejercicio 9. Escriba un programa que pida dos números enteros. El programa pedirá de nuevo
# el segundo número mientras no sea mayor que el primero. El programa terminará escribiendo
# los dos números.

def mayor_que(a, b):
    """
    Docstring para mayor_que
    
    :param a: Descripción
    :param b: Descripción
    """
    while b <= a:
        b = int(input(f"El segundo numero debe ser mayor al primero ({a}): "))
    print(f"Ingresate {a} y {b}")

def main():
    a = int(input("Ingresa el primer numero entero: "))
    b = int(input("Ingresa el segundo numero entero: "))
    mayor_que(a, b)

if __name__ == "__main__":
    main()