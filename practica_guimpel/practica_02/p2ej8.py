# Ejercicio 8. Escriba un programa que permita al usuario ingresar un
# conjunto de notas, preguntando a cada paso si desea ingresar más notas, 
# e imprima el promedio correspondiente al finalizar la toma de datos.

"""
Representamos un conjunto de notas como una lista de números reales positivos entre 0 y 10.
"""

def nota_valida(nota): # Función pura
    """
    nota_valida: Float -> Bool
    Devuelve True si la nota está entre 0 y 10, False en caso contrario.
    Ejemplos:
    entrada: 10, salida: True
    entrada: 0, salida: True
    entrada: -1, salida: False
    entrada: 11, salida: False
    """
    return 0 <= nota <= 10

def promedio(notas): # Función pura
    """
    promedio: list[float] -> float
    Recibe una lista de notas y devuelve su promedio.
    Se asume que la lista tiene al menos un elemento.
    Ejemplo:
    entrada: [4, 8, 7, 10], salida: 7.25
    """
    return sum(notas) / len(notas)

def pedir_nota(numero):
    """
    pedir_nota: Int -> Float
    Pide al usuario la nota 'numero', valida que esté entre 0 y 10
    y la devuelve como float.
    """
    nota = float(input(f"Ingresá la nota número {numero}: "))
    while not nota_valida(nota):
        nota = float(input(f"Error. Volvé a ingresar la nota {numero} (entre 0 y 10): "))
    return nota

def pedir_notas():
    """
    pedir_notas: None -> List[float]
    Pide al usuario tantas notas como desee ingresar.
    Devuelve la lista de notas ingresadas.
    Cualquier cosa distinta de 'N' se interpreta como seguir.
    """
    notas = []
    seguir = input("¿Desea ingresar una nota? (S/N): ").upper()

    while seguir != "N":
        nota = pedir_nota(len(notas) + 1)
        notas.append(nota)
        print("¡Nota registrada!")
        seguir = input("¿Desea ingresar otra nota? (S/N): ").upper()
        
    return notas

def main():
    """
    Programa principal:
    - Pide notas al usuario
    - Calcula el promedio
    - Lo imprime en pantalla
    """
    notas = pedir_notas()

    if len(notas) > 0:
        prom = promedio(notas)
        print(f"El promedio es: {prom}")
    else:
        print("No se ingresaron notas.")


if __name__ == "__main__":
    main()