# --------------------------------------------------------
# Programa para calcular la hipotenusa de un triangulo
# rectangulo dado los catetos del mismo.
# Tobias Maggiori
# 12 de marzo del 2024
# --------------------------------------------------------


def raiz_cuadrada(radicando):
	"""
	Diseño de datos:
	 radicando: float
	Signatura:
	 raiz_cuadrada: float -> float
	Proposito:
	 Calcula la raiz cuadrada de un numero real dado.
	Ejemplos:
	raiz_cuadrada(81) = 9
	raiz_cuadrada(16) = 4
	"""
	return radicando**0.5

def test_raiz_cuadrada():
	assert raiz_cuadrada(81) == 9
	assert raiz_cuadrada(1) == 1
	assert raiz_cuadrada(0) == 0

def pitagoras(a,b):
	"""
	Diseño de datos:
	 a: float
	 b: float
	Signatura:
	 pitagoras : float float -> float
	Proposito:
	 Calcula la raiz cuadrada de la suma
	 de los cuadrados de dos numeros reales datos.
	Ejemplos:
	 pitagoras(16,16) = 22.627417 
	"""
	hipotenusa = raiz_cuadrada(a*a+b*b)
	return hipotenusa

def test_pitagoras():
	assert pitagoras(16,16) == 22.627416997969522

def main():
	print("Programa para calcular la hipotenusa de un triangulo rectangulo.")
	a = float(input("Por favor, ingrese el cateto a del triangulo rectangulo."))
	b = float(input("Por favor, ingrese el cateto b del triangulo rectangulo."))
	print(f"La hipotenusa del triangulo rectangulo de lado {a} y lado {b} es", pitagoras(a,b))

if __name__ == '__main__':
	main()
