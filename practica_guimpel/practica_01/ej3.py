def n_mayores_m(n=26, m=25):
    """Imprime los primeros numeros n mayores que m
    n_mayores_m : Int Int -> None"""
    if n == 0:
        return
    print(m+1)
    n_mayores_m(n-1, m+1)


# La anterior funcion no es testeable y por lo tanto su definicion no es de buena practica.
# A continuacion presento una version testeable, que puede aplicarse a ej1.py y ej2.py

def n_mayoresm(n=25, m=0):
    """Devuelve un string con los primeros n números mayores que m,
    uno debajo del otro."""
    if n == 0:
        return ""
    if n == 1:
        return str(m + 1)
    return str(m + 1) + "\n" + n_mayoresm(n - 1, m + 1)

print(n_mayoresm(n=26, m=25))

