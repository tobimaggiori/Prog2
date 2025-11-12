def primeros_n_pares(x=1, n=25):
    """Imprime los primeros n naturales pares.
    primeros_n_pares: Int Int -> None"""
    if x > n:
        return
    print(x*2)
    primeros_n_pares(x+1)


primeros_n_pares()