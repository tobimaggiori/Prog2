# Ejercicio 5. Usando la función dada como ejemplo en la presentación de La Receta en Python
# para convertir una temperatura de Fahrenheit a Celsius, genere una tabla de conversión de
# temperaturas, desde 0 ◦F hasta 120◦F, de 10 en 10.

# Función mencionada en la consigna:
def farCel(f):
    return (f-32)*5/9

"""
Desarrollo la consigna en la función main, ya que realizarla como una función a parte no lo veo
bueno dado que sería una función que no devuelve nada sino que imprime en pantalla.
"""
def main():
    for x in range(0, 13):
        print(farCel(x*10)) #tambien podria haber usado range(0, 121, 10) y no pasar x*10 aca

if __name__ == '__main__':
    main()