"""
Programa para calcular el perimetro de un circulo
a partir de su radio.
"""
pi = 3.141592 # valor del numero PI.

def perimetro_circ(radio):
	"""
	radio (cm): float
	perimetro (cm): float
	perimetro_circ : float -> float
	Calcula el perimetro de un circulo 
	en base al valor del radio dado.
	"""
	perimetro = 2 * pi * radio
	return perimetro

def test_perimetro_circ():
	assert perimetro_circ(15) == 94.24776

def main():
	print("Programa para calcular perimetro de un circulo.")
	radio = float(input("Ingrese el radio del circulo: "))
	print("El perimetro del circulo es: ", perimetro_circ(radio))

if __name__ == '__main__':
	main()

"""
Programa para calcular el area
de un circulo a partir de su radio.
"""	
	
def area_circ(radio):
	"""
	radio (cm): float
	area (cm): float
	area_circ : float -> float
	Calcula y devuelve el area de un circulo
	en base al valor del radio dado.
	"""
	area = pi * radio * radio
	return area

def test_area_circ():
	assert area_circ(15) == 706.8582

def main2():
	print("Programa para calcular area de un circulo.")
	radio = float(input("Ingrese el radio del circulo: "))
	print("El area del circulo es: ", area_circ(radio))

if __name__ == '__main__':
	main2()
	
