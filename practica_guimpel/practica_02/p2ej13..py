# a) Escriba una función es_potencia_de_dos que reciba como parámetro un número natural
# y devuelva True si el número es una potencia de 2 y False en caso contrario.

# b) Escriba una función que, dados dos números naturales pasados como parámetros,
# devuelva la suma de todas las potencias de 2 que hay en el rango formado por esos números
# (0 si no hay ninguna potencia de 2 entre los dos). Utilice la función es_potencia_de_dos 
# descripta en el punto anterior.

"""
a es potencia de b si existe k entero positivo tal que b^k = a
Ejemplo:
8 es potencia de 2 porque 2^3 = 8.
"""

""" def es_potencia_de_dos(n):
####
    es_potencia_de_dos: Natural -> Bool
    Recibe un numero natural y devuelve True si es potencia de 2
    o False si no lo es.
    Ejemplos:
    entrada: 8, salida: True
    entrada: 5, salida: False
    entrada: 32, salida: True
#####
    es_potencia = False # Asumimos que no es potencia de 2.
    for i in range(1, n):
        if 2 ** i == n:
            es_potencia = True
    return es_potencia
"""

# Esta version con FOR no es muy eficiente. A continuacion, se presenta la version más eficiente:
def es_potencia_de_dos(n):
    """
    es_potencia_de_dos: Natural -> Bool
    Devuelve True si n es potencia de 2, False en caso contrario.
    """
    es_potencia = False # Asumimos que no es potencia de 2.

    if n > 0:   # Caso 0: por definición, 0 NO es potencia de 2
        potencia = 1   # representa 2^0
        # multiplicamos por 2 hasta superar o igualar n
        while potencia < n:
            potencia = potencia * 2
        if potencia == n:
            es_potencia = True

    return es_potencia

def suma_potencias_de_dos(a, b):
    """
    suma_potencia_de_dos: Natural Natural -> Natural
    Dado dos numeros naturales a y b, devuelve la suma de las potencias
    de dos comprendidas entre el intervalo [a, b).
    Ejemplo:
    entrada: 4, 10, salida: 12
    entrada: 4, 20, salida: 28
    entrada: 5, 8, salida: 0
    """
    suma = 0
    for i in range(a, b):
        if es_potencia_de_dos(i) == True:
            suma = i + suma
    print(suma)


"""Esta version con while es mas eficiente porque multiplicar por 2 crece muy rápido:
1, 2, 4, 8, 16, 32, 64, 128… por lo tanto alcanza a n con muy pocas iteraciones.
Ejemplos:
si n = 32 → 6 iteraciones
si n = 1.000.000 → 20 iteraciones
si n = 1.000.000.000 → 30 iteraciones
"""

suma_potencias_de_dos(5, 8)