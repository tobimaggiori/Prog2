// Escriba una función que lea la nota de un alumno (entera) y muestre un mensaje
// diciendo si sacó insifuciente (2 a 5), aprobado (6), bueno (7), muy bueno (8), distinguido (9)
// o sobresaliente (10). Se debe mostrar un mensaje de error si la nota ingresada no es válida.
// Este programa debe hacerse de dos maneras diferentes: con if secuenciales y con if-else anidados.
#include <stdio.h>
// Version if-else anidados. \\ SIRVE DE EJEMPLO IF SECUENCIALES
int main(){
    int nota;
    printf("Ingrese la nota del alumno: ");
    scanf("%d", &nota);

    if (nota < 2 || nota > 10) { // Este caso podria realizarse en un else
        printf("Nota no valida\n");  // pero se piden if anidados.
    }
    if (nota >= 2 && nota <= 5) {
        printf("Insuficiente\n");
    }

    if (nota == 6) {
        printf("Aprobado\n");
    }

    if (nota == 7) {
        printf("Bueno\n");
    }

    if (nota == 8) {
        printf("Muy bueno\n");
    }

    if (nota == 9) {
        printf("Distinguido\n");
    }

    if (nota == 10) {
        printf("Sobresaliente\n");
    }
    
    return 0;
}