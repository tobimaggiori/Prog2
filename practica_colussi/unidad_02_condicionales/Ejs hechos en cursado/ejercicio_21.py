# Programa que permite clasificar 23 notas de un examen de 
# distintos alumnos ingresadas por un auxiliar docente.
# Las notas se clasifican de acuerdo a lo establecido en 
# el diseño de datos de la funcion "clasificar_nota".
# Tobias Maggiori - LCC. PROGRAMACION II. 
# 28 de marzo de 2024.

def clasificar_nota(nota):
    """
    clasificar_nota : Float -> String
    Diseño de datos:
        nota alumno: numero real entre 1 y 10 inclusives.
    Proposito:
        Dada una nota de un examen de un alumno devuelve:
        "Insuficiente" si 1 <= nota < 4
        "No Aprobado" si 4 <= nota < 6
        "Aprobado" si 6 <= nota < 8
        "Muy Bueno" si 8 <= nota < 10
        "Exelente" si nota = 10
    Ejemplos:
        clasificar_nota(1) == "Insuficiente"
        clasificar_nota(4) == "No Aprobado"
        clasificar_nota(6) == "Aprobado"
        clasificar_nota(8) == "Muy Bueno"
        clasificar_nota(10) == "Excelente"
    """
    if nota >= 1 and nota < 4:
        mensaje = "Insuficiente"
    elif nota >= 4 and nota < 6:
        mensaje = "No Aprobado"
    elif nota >= 6 and nota < 8:
        mensaje = "Aprobado"
    elif nota >= 8 and nota < 10:
        mensaje = "Muy Bueno"
    else:
        mensaje = "Excelente"
    return mensaje

def test_clasificar_nota():
    assert clasificar_nota(1) == "Insuficiente"
    assert clasificar_nota(4) == "No Aprobado"
    assert clasificar_nota(6) == "Aprobado"
    assert clasificar_nota(8) == "Muy Bueno"
    assert clasificar_nota(10) == "Excelente"

def main():
    for i in range(1,24):
        nota = float(input(f"Ingrese la nota del/la {i} alumno/a: "))
        if 1 <= nota and nota <= 10:
            nota = nota
        else:
            print("Por favor, ingrese una nota entre 1 y 10.")
            nota = float(input(f"Ingrese la nota del/la {i} alumno/a: "))
        print(f"La clasificación del/la {i} alumno/a es {clasificar_nota(nota)}")

if __name__ == '__main__':
    main()