# ---------------------------------------------------------------------------
# Programa que permite clasificar el promedio de un cuatrimestre de 
# distintos alumnos a partir de las notas ingresadas por un auxiliar docente.
# El promedio se clasifica de acuerdo a lo establecido en 
# el diseño de datos de la funcion "clasificar_promedio".
# Tobias Maggiori - LCC. PROGRAMACION II. 
# 28 de marzo de 2024.
# ---------------------------------------------------------------------------
# Comentario:
# Contemple los 3 items del ejercicio haciendo este programa
# de forma generica, para que el docente auxiliar ingrese
# cuantos alumnos tiene y cuantas notas por cada alumno quiere ingresar.
# ---------------------------------------------------------------------------
def calcular_promedio(b):
    """
    promedio: Integer -> Float
    
    Solicita al operador b notas y calcula el promedio de estas.
    """
    suma_notas = 0
    promedio = 0
    for i in range(1,b+1):
        nota = float(input(f"Ingrese la {i} nota: "))
        suma_notas = nota + suma_notas
    promedio = suma_notas / b
    return promedio

def clasificar_promedio(promedio):
    """
    clasificar_promedio: Float -> String
    Diseño de datos:
        promedio alumno: numero real entre 1 y 10 inclusives.
    Proposito:
        Dado el promedio del cuatrimestre de un alumno, devuelve:
        "Insuficiente" si 1 <= promedio < 4
        "No Aprobado" si 4 <= promedio < 6
        "Aprobado" si 6 <= promedio < 8
        "Muy Bueno" si 8 <= promedio < 10
        "Exelente" si promedio = 10
    Ejemplos:
        clasificar_promedio(1) == "Insuficiente"
        clasificar_promedio(4) == "No Aprobado"
        clasificar_promedio(6) == "Aprobado"
        clasificar_promedio(8) == "Muy Bueno"
        clasificar_promedio(10) == "Excelente"
    """
    if promedio >= 1 and promedio < 4:
        mensaje = "Insuficiente"
    elif promedio >= 4 and promedio < 6:
        mensaje = "No Aprobado"
    elif promedio >= 6 and promedio < 8:
        mensaje = "Aprobado"
    elif promedio >= 8 and promedio < 10:
        mensaje = "Muy Bueno"
    else:
        mensaje = "Excelente"
    return mensaje
      
def test_clasificar_promedio():
    assert clasificar_promedio(1) == "Insuficiente"
    assert clasificar_promedio(4) == "No Aprobado"
    assert clasificar_promedio(6) == "Aprobado"
    assert clasificar_promedio(8) == "Muy Bueno"
    assert clasificar_promedio(10) == "Excelente"
    
def main():
    c = int(input("¿De cuantos alumnos/as desea clasificar sus promedios? : "))
    b = int(input("¿Cuantas notas por alumno desea ingresar?: "))
    for a in range(1,c+1):
        print(f"A continuación ingrese las {b} notas del cuatrimestre del {a} alumno/a:")
        print(f"La clasificacion del promedio del {a} alumno/a es: {clasificar_promedio(calcular_promedio(b))}.")

if __name__ == '__main__':
    main()