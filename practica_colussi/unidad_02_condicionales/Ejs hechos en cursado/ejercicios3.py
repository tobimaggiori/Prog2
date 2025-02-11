def factorial_ite (num):
    """ Número: Natural .
    Nat ->Nat
    Calcular en forma iterativa el factorial de un número natural dado.
    factorial_ite (5) = 120, factorial_ite (0) = 1, factorial_ite (1) = 1
    """
    fact = 1
    for i in range (2,num +1):
        fact = fact * i
    return fact

def test_factorial_ite():
    assert factorial_ite(0) == 1
    assert factorial_ite(1) == 1
    assert factorial_ite(5) == 120

def factorial_rec (n):
    """ Número: Natural .
    Nat ->Nat
    Calcular en forma recursiva el factorial de un número natural dado.
    factorial_rec (5) = 120, factorial_rec (0) = 1, factorial_rec (1) = 1
    """
    if n == 0:
        return 1
    else:
        return n* factorial_rec (n -1)
    

def main ():
    valor = int (input (" Ingrese un valor natural para cualcular su factorial : "))
    print("El factorial de ", valor , "es ", factorial_rec (valor))

main ()
