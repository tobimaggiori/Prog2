# Usamos el tipo de dato 'Tiempo' para modelar un horario.
# Tiempo es (Hora, Minutos, Segundos) donde:
# Hora es un numero de dos digitos perteneciente a [00;23]
# Minutos es un numero de 1 a 2 digitos perteneciente a [0;60]
# Segundos es un numero de 1 a 2 digitos perteneciente a [0;60]
# Por ejemplo, Tiempo es (10, 2, 59) y es la hora 10:02:59.

def crear_tiempo(hora, minutos, segundos):
    while hora not in range(00, 24):
        hora = int(input("Valor incorrecto para hora, ingrese un valor entre 00 y 23: "))
    while minutos not in range(00, 61):
        minutos = int(input("Valor incorrecto para minutos, ingrese un valor entre 00 y 60: "))
    while segundos not in range(00, 61):
        segundos = int(input("Valor incorrecto para segundos, ingrese un valor entre 00 y 60: "))
    return (hora, minutos, segundos)

def suma_tiempo(tiempo1, tiempo2):
    hora1, minutos1, segundos1 = tiempo1
    hora2, minutos2, segundos2 = tiempo2
    h_suma = (hora1 + hora2) % 24 #Suma las horas. Ver como sumar Minutos y segundos con chatgpt. Entender.
    for i in range(1,3):
            if tiempo1[i] + tiempo2[i] == 60:
                aux = 00
            elif (tiempo1[i] + tiempo2[i]) > 60:
                aux = (tiempo1[i] + tiempo2[i]) - 60
            else:
                aux = (tiempo1[i] + tiempo2[i])
            if i == 1:
                minutos = aux
            else:
                segundos = aux
    return (crear_tiempo(h_suma, minutos, segundos))

def main(horario1=0, horario2=0):
    print("Programa para sumar o restar dos horarios")
    print("Acontinuación ingrese los datos del primer horario a operar:")
    for i in range(1,3):
        hora = int(input(f"Ingrese la hora para el horario {i}: "))
        minutos = int(input(f"Ingrese los minutos para el horario {i}: "))
        segundos = int(input(f"Ingrese los segundos para el horario {i}: "))
        if i == 1:
            horario1 = crear_tiempo(hora, minutos, segundos)
        else:
            horario2 = crear_tiempo(hora, minutos, segundos)
    accion = input("¡Genial! ahora ingrese S para sumar o R para restar los horarios: ").upper()
    if accion == "S":
        horario_suma = suma_tiempo(horario1, horario2)
        hora_suma, minutos_suma, segundos_suma = horario_suma
        print(f"La suma de los horarios ingresados es: {hora_suma:02}:{minutos_suma:02}:{segundos_suma:02}")

if __name__ == "__main__":
    main()



