def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    return a / b

def main():
    # En todo lo siguiente, deberia haber una validacion de tipo de datos.
    op = input("""Ingresá una opción:
            1. Suma
            2. Resta
            3. Multiplica
            4. Divide
               """)
    a = int(input("Ingresá el primer valor: "))
    b = int(input("Ingresá el segundo valor: "))
    if op == "1":
        print(f"{a} + {b} = {suma(a,b)}")
    elif op =="2":
        print(f"{a} - {b} = {resta(a,b)}")
    elif op == "3":
        print(f"{a} * {b} = {multiplica(a,b)}")
    elif op == "4":
        print(f"{a} / {b} = {divide(a,b)}")
    else:
        print("Opción no reconocida!")
        main()
    seguir = input("Desea seguir operando? (si/no): ").lower()
    if seguir == 'si':
        main()
            


        
        

if __name__ == '__main__':
    main()