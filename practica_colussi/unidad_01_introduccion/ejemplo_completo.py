#-----------------------------------
# Este programa calcula el area de un triangulo dado sus 3 lados
# Catedra Programacion II, 2C.
# Universidad Nacional de Rosario
# 

def area_triangulo(base, altura):
    ''' 
    Base (cm): float
    Altura (cm): float
    Area (cm): float
    area_triangulo: float float -> float
    area triangulo calcula el area de un triangulo en base a los datos dados.
    Ejemplo:
    '''
    area = ((base * altura)/ 2)
    return area

def test_area_triangulo():
    assert (round (area_triangulo(3.16, 4.43), 4) == 6.9994)    # round redondea el resultado con 4 decimales.
    assert (round (area_triangulo(2, 2), 1) == 2.0) # round redondea el resultado con 1 decimal.
    assert (round (area_triangulo(5.1, 2.75), 15) == 7.012499999999999) # round redondea el resultado con 15 decimales.

def main():
    print("Programa para calcular el Area de un Triangulo")
    base = float(input("Ingrese la longitud de la base:"))
    altura = float(input("Ingrese la longitud de la altura: "))
    print("El area del triangulo es: ", area_triangulo(base, altura))

if __name__ == '__main__':
    main()


