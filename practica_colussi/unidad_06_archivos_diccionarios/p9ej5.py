"""
Ejercicio 5. Escribir un programa, llamado head.py que reciba un archivo y un número N e imprima
las primeras N líneas del archivo.
"""


def leerImprimir(archivo, n):
        f = open(archivo, 'r')
        for i in range(0, n):
            linea = f.readline()
            print(linea)
    
# FALTA RECETA Y MAIN PARA LLAMAR A LA FUNCION
# QUE MAIN RECIBA NOMBRE DE ARCHIVO Y NUMERO N.

leerImprimir("/home/tobias/Onedrive/LCC/Primer Año/Programación 2 FCEIA/practica_9/prueba.txt", 3)