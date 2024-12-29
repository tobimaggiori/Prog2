# Ejs 1, 2 y 3. 
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
imprimir_pares(25, 10)
