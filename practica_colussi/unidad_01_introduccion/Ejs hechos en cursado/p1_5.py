"""
Programa para calcular el factorial de un numero natural.
"""

def factorial(n):
	"""
	Signatura:
	 factorial: Natural -> Natural
	Proposito:
	 Calcula el factorial de un numero natural dado.
	Ejemplos:
	 factorial(5) = 120
	 factorial(0) = 1
	"""
	if n == 0:
		return 1
	else:
		fact = n * factorial(n-1)
		return fact

def test_factorial(n):
	assert factorial(5) == 120
	assert factorial(1) == 1
	assert factorial(0) == 1

def main():
	print("Programa para calcular el factorial de un numero natural.")
	n = int(input("Ingrese el numero del cual desea su factorial: "))
	print(f"El factorial de {n} es: ", factorial(n))

if __name__ == '__main__':
	main()
