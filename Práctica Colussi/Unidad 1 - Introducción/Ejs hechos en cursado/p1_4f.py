"""
Este programa calcula el volumen de una esfera a partir de su radio.
"""
PI = 3.141592

def volumen_esfera(radio):
	"""
	radio (en X unidad de medida): float
	volumen (en misma X unidad): float
	
	volumen_esfera: float -> float
	
	Devuelve el valor del volumen de una esfera,
	dado el radio que recibe.
	"""
	vol_esfera = (4/3) * PI * (radio**3)
	return vol_esfera

def test_volumen_esfera():
	assert volumen_esfera(15) == 14137.163999999999

def main():
	print("Programa para calcular el volumen de una esfera.")
	radio = float(input("Por favor ingrese el radio de la esfera: "))
	print("El volumen de la esfera es: ", volumen_esfera(radio))

if __name__ == '__main__':
	main()
