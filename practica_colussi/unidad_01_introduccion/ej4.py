# La idea es hacer funciones testeables, funciones que solo calculen una cosa y bien.
# Por ejemplo, hacer una funcion que calcule area y perimetro no es modularizar,
# en cambio una funcion que calcule area y otra el perimetro si.
# La validacion de los datos de entrada y demas, siempre en la funcion principal.
# Las funciones testeables no manejan entradas de datos.
# Las funciones testeables devuelven algun tipo de dato; no imprimen en pantalla.
# Por otro lado
# La idea de no usar variables globales es que cada función sea predecible: 
# solo depende de sus parámetros y de lo que define dentro.

def perimetro_rectangulo(base, altura):
    '''
    base (cm): float
    altura (cm): float
    perimetro (cm): float
    perimetro_rectangulo: float float -> float float
    Dada la base y la altura de un rectangulo, devuelve su perimetro.
    Ejemplo:
    perimetro_rectangulo(4, 2) = 12
    '''
    return 2*base + 2*altura

def test_perimetro_rectangulo():
    assert perimetro_rectangulo(4, 2) == 12

def area_rectangulo(base, altura):
    '''
    base (cm): float
    altura (cm): float
    area (cm^2): float
    area_rectangulo: float float -> float
    Dada la base y la altura de un rectangulo devuelve su area.
    Ejemplo:
    area_rectangulo(4, 2) = 8
    '''
    return base * altura

def test_area_rectangulo():
    assert area_rectangulo(4, 2) == 8

# Item c) Calcular el perímetro y el área de un rectángulo (alineado con los ejes x e y) dadas sus
# coordenadas x1, x2, y1, y2.
# Al hacer el analisis del problema para plantear el diseño de datos, pensamos en
# Que significa que el rectangulo este alineado con los ejes x e y?
# que la altura forme una recta derecha con el eje x y la base una recta derecha con el eje y.
# Al plantear este dibujo y darle incognitas a los 4 puntos: simplemente devemos calcular:
# base = |x2 - x1| , altura = |y2 - y1|. Queremos la distancia entre dos puntos de la recta.
# REALIZADO EN LA FUNCION MAIN.

# -------------------------------------------------------------------------------
# Item d) Calcular el perímetro de un círculo dado su radio. Ayuda: Considerar a PI como 3,141592.
def perimetro_circulo(radio):
    '''
    perimetro_circulo: float -> float
    Recibe el radio de un circulo y devuelve su perimetro redondeado a dos decimales.
    Ejemplo:
    perimetro_circulo(5) = 31.42
    '''
    PI = 3.141592
    return 2*PI*radio

def test_perimetro_circulo():
    assert round(perimetro_circulo(5), 2) == 31.42

# -------------------------------------------------------------------------------
# Item e) Área de un círculo dado su radio.
def area_circulo(radio):
    '''
    area_circulo: float -> float
    Devuelve el area de un circulo dado su radio.
    '''
    PI = 3.141592
    return PI*radio*radio

def test_area_circulo():
    assert round(area_circulo(5), 2) == 78.54

# -------------------------------------------------------------------------------
# f) Calcular el volumen de una esfera dado su radio.
def volumen_esfera(radio):
    '''
    volumen_esfera: float -> float
    Dado el radio de una esfera devuelve su volumen.
    Ejemplo:
    volumen_esfera(5) = 523.6
    '''
    PI = 3.14159
    return (4/3)*PI*radio*radio*radio

def test_volumen_esfera():
    assert round(volumen_esfera(5)) == 524

# -------------------------------------------------------------------------------
# Item g) los catetos de un triangulo rectangulo; calcular su hipotenusa.
def raiz_cuadrada(x):
    '''
    raiz_cuadrada: float -> float
    Dado un numero real positivo x, devuelve su raiz cuadrada.
    Ejemplo:
    raiz_cuadrada(4) == 2
    '''
    return x ** 0.5  # Hallar la raiz cuadrada de x es lo mismo que elevarlo por 1/2

def test_raiz_cuadrada():
    assert raiz_cuadrada(4) == 2


def main():
    x1 = float(input("Ingresa el valor x1: "))
    x2 = float(input("Ingresa el valor x2: "))
    y1 = float(input("Ingresa el valor y1: "))
    y2 = float(input("Ingresa el valor y2: "))
    base = abs(x2 - x1)
    altura = abs(y2 - y1)
    print(f"""El perimetro del rectangulo es: {perimetro_rectangulo(base, altura)}, 
          y su área es {area_rectangulo(base, altura)}""")
    
    # Item g)
    q = input("Desea calcular la hipotenusa de un triangulo rectangulo? (si/no): ")
    if q == 'si':
        a = float(input("Ingresa la longitud del cateto a: "))
        b = float(input("Ingresa la longitud del cateto b: "))
        print(f"La longitud de la hipotenusa es", raiz_cuadrada(a*a + b*b))

if __name__ == '__main__':
    main()