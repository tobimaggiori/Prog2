# Ejercicio 7. Escriba una función que le pida al usuario que ingrese un número positivo. Si el
# usuario ingresa cualquier cosa que no sea lo pedido se le debe informar de su error mediante
# un mensaje y volver a pedirle el número, repitiendo este proceso hasta que ingrese lo pedido.

def validar():
    """
    validar : None -> None
    Le pide al usuario el ingreso de un nro positivo hasta que
    efectivamente ingrese un numero positivo.
    """
    n = float(input("Ingresá un número positivo: "))
    while n <= 0:
        n = float(input("Error. Ingresá un número positivo: "))
    print("Bien hecho")

validar()