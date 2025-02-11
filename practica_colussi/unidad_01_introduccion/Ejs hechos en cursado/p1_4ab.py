# a) calcular el perímetro de un ractángulo
# dada su base y su altura.
"""
base (cm): float
altura (cm): float
perimetro (cm): float
perimetro_rect : Number Number -> Number
Calcula el perimetro de un rectangulo en base a los datos dados. 
"""
def perimetro_rect(b,h):
    perimetro = 2*b + 2*h
    return perimetro

def test_perimetro_rect():
    assert perimetro_rect(5,5) == 20
    assert perimetro_rect(3,2) == 10
    
# b) Calcular el área de un rectángulo dada su base y su altura.
"""
base (cm): float
altura (cm): float
area (cm): float
area_rect : Number Number -> Number
Calcula el area de un rectangulo en base a los datos datos.
"""
def area_rect(base,altura):
	area = base * altura
	return area

def test_area_rect():
	assert test_area_rect(5,5) == 25
	assert test_area_rect(8,9) == 72

def main():
    print("Programa para calcular perimetro y area de un rectangulo.")
    base = float(input("Por favor, ingrese la base del rectangulo (cm): "))
    altura = float(input("Por favor, ingrese la altura del rectangulo (cm): "))
    print("El numero de perimetro es: ", perimetro_rect(base,altura))
    print("El numero de area es: ", area_rect(base,altura))
    
if __name__ == '__main__':
    main()
    
