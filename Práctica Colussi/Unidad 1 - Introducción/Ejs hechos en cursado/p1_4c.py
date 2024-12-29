"""
largo (cm): float
alto (cm): float
perimetro (cm): float
perimetro_rect : Number Number -> Number
perimetro_rect devuelve el perimetro de un rectangulo dado su largo y alto.
"""
def perimetro_rect(largo,alto):
	perimetro = 2*largo + 2*alto
	return perimetro
	
def test_perimetro_rect(largo, alto):
	assert perimetro_rect(10,10) == 40

"""
largo (cm): float
alto (cm): float
area (cm): float
area_rect : Number Number -> Number
area_rect devuelve el area de un rectangulo dado su largo y alto.
"""	
def area_rect(largo,alto):
	area = largo * alto
	return area

def test_area_rect(largo,alto):
	assert area_rect(10,10) == 100
	
def main():
	print("Programa para calcular el perimetro y area de un rectangulo dadas sus coordenadas del plano")
	x1 = float(input("Ingrese la coordenada X1 del rectángulo: "))
	x2 = float(input("Ingrese la coordenada X2 del rectángulo: "))
	y1 = float(input("Ingrese la coordenada Y1 del rectángulo: "))
	y2 = float(input("Ingrese la coordenada Y2 del rectángulo: "))
	largo = x2 - x1
	alto = y2 - y1
	print("El perimetro del rectangulo es: ", perimetro_rect(largo, alto), "y el area es: ", area_rect(largo,alto))

if __name__ == '__main__':
	main()


