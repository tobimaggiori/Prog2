import random

def tirar_dado():
    return random.randint(1,6)

def jugar_dado():
    dado = 0
    lanzamientos = 0
    
    while dado != 6:
        print("Tirando el dado...")
        dado = tirar_dado()
        print("Resultado: ", dado)
        lanzamientos += 1

    print(f"El dado se lanzó {lanzamientos} veces.")

jugar_dado()