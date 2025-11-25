# Ejercicio 2. Escriba un programa que imprima por
# pantalla todas las fichas del dominó, una por línea y sin repetir.
# ----------------------------------------------------------------------
"""
Este programa imprime en pantalla las 28 fichas del dominó, una debajo
de otra y sin repetir las mismas.

Representación de datos:
Una ficha es una lista, de longitud 2, de números enteros entre 0 y 6.
Por ejemplo: la ficha [0, 6] represena la ficha del dominó con 0 pips
en un lado y 6 pips en el otro lado. Los lados son indiferentes, la
ficha [0, 6] es igual a la ficha [6, 0].
"""
def main():
    domino = [[i, j] for i in range(7) for j in range(i, 7)] # Def. por comprension.
    # Notar que el segundo for es ejecutado por el primero.
    for x in domino:
        print(x)

if __name__ == '__main__':
    main()

# Pensando la lista domino: Iteraciones del primer for:
# Primer iteracion: i-> 0 luego el segundo for le va asignando a j los naturales del i=0 inc. hasta el 6 inc.
# Segunda iteracion: i-> 1 luego el segundo for le va asignando a j los naturales del i=1 inc. hasta el 6 inc.
# Tercera iteracion: i-> 2 luego el segundo for le va asignando a j los naturales del i=2 inc. hasta el 6 inc.
# . . .
# Septima iteracion: i-> 6 luego el segundo for le asigna a j, en su única iteración, el 6.