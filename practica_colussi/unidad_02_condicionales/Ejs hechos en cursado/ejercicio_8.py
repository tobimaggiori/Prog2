# Ejercicio 8. Diseñar un programa, que utilizando funciones matemáticas, calcule las raíces
# reales (no las complejas) de un polinomio de segundo grado.
# Nota: validar que las operaciones puedan efectuarse antes de realizarlas (no dividir por cero,ni
# calcular la raíz de un número negativo). La función no tienen que devolver nada, simplemente
# puede mostrar por pantalla el resultado del cálculo.

def discriminante(a, b , c):
    return ((b**2) - 4 * a * c)

def raices_reales(a, b, c):
    """
    raices_reales: Number Number Number -> None
    """
    if discriminante(a,b,c) > 0 and a != 0:
        raiz1 = (-b + ((discriminante(a,b,c))**0.5)) / (2 * a)
        raiz2 = (-b - ((discriminante(a,b,c))**0.5)) / (2 * a)
        print(f"Las raices del polinomio cuadratico ingresado son {raiz1} y {raiz2}.")
    else:
        print("a es igual a 0 o el discriminante es negativo.")
    
# print(raices_reales(1, 4, -5))

