# a) Escriba un programa que contenga una contraseña inventada. 
# El programa debe preguntarle al usuario la contraseña y no 
# permitirle continuar hasta que la haya ingresado correctamente.

# b) Modifique el programa anterior para que solamente permita como máximo una cantidad
# fija de intentos.

# c) Modifique el programa anterior para que sea una función que devuelva
# si el usuario ingresó la contraseña correctamente o no, mediante un valor booleano (True o False).

# Item a), dado que el programa no continua hasta que ingrese la contraseña: while

def validarpass(contra, password):
    """
    validarpass: String String -> Boolean
    Recibe dos String y los compara, si son iguales devuelve True,
    de lo contrario vuelve a solicitar 'contra' hasta ser igual a 'password'.
    """
    while contra != password:
        print("La contraseña ingresada es incorecta.")
        contra = input("Por favor, volve a intentarlo: ")
    return True

# Item b): cantidad fija de intentos: bucle for.
def validarpass_for(contra, password):
    """
    validarpass_for: String String -> Boolean
    Recibe dos String y los compara, si son iguales devuelve True,
    de lo contrario vuelve a solicitar 'contra' hasta ser igual a 'password' 3 veces.
    Superado los 3 intentos devuelve False.
    """
    for i in range(1, 4):
        if contra != password:
            print("La contraseña ingresada es incorecta.")
            contra = input(f"Intento {i} de 3, volvé a intentarlo: ")
        else:
            return True
    return False

def main():
    contra = input("Ingresá la contraseña: ")
    if validarpass_for(contra, "password") == True:
        print("Bienvenido al programa.")
    else:
        print("Su usuario se ha bloqueado por seguridad, contacte al administrador.")
        return
    print("Sección en desarollo...")


if __name__ == "__main__":
    main()

# El item c ya esta realizado en los item a y b.
