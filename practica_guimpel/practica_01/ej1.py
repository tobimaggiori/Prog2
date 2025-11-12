def primeros_25_pares(x=1):
    """Imprime los primeros 25 naturales pares.
    primeros_25_pares: int -> None"""
    if x > 25:
        return
    print(x*2)
    primeros_25_pares(x+1)


primeros_25_pares()