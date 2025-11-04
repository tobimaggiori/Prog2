# Este programa le pide al usuario su nombre y lo saluda,
# dos numreos y le muestra el producto.

def username(name):
    '''
    Nombre del usuario: String
    username: String -> String
    Recibe el nombre de usuario y devuelve un saludo.
    Ejemplo:
    username(tobi) = "Bienvenido tobi"
    '''
    saludo = f'Bienvenido {name}'
    return saludo

def test_username():
    assert username("tobi") == "Bienvenido tobi"
    assert username("turing") == "Bienvenido turing"

def producto(a, b):
    '''
    producto: float -> float
    Dado dos numeros devuelve su producto.
    Ejemplo:
    producto(2, 2) = 4
    producto(5, 1/5) = 1
    '''
    return a * b

def test_producto():
    assert producto(2, 2) == 4
    assert producto(5, 1/5) == 1

def main():
    name = input("Ingresé su usuario: ")
    print(username(name))
    a = float(input("Ingresá el primer valor: "))
    b = float(input("Ingresá el segundo valor: "))
    print(f'El producto de {a} {b} es {producto(a, b)}')

if __name__ == '__main__':
    main()
