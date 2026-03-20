// Escriba una función que lea la nota de un alumno (entera) y muestre un mensaje
// diciendo si sacó insifuciente (2 a 5), aprobado (6), bueno (7), muy bueno (8), distinguido (9)
// o sobresaliente (10). Se debe mostrar un mensaje de error si la nota ingresada no es válida.
// Este programa debe hacerse de dos maneras diferentes: con if secuenciales y con if-else anidados.
#include <stdio.h>
// Version if-else anidados. \\ SIRVE DE EJEMPLO IF-ELSE ANIDADOS
int main(){
    int nota;
    printf("Ingrese la nota del alumno: ");
    scanf("%d", &nota);
if (nota >= 2 && nota <= 5) {
    printf("Insuficiente\n");
} else {
    if (nota == 6) {
        printf("Aprobado\n");
    } else {
        if (nota == 7) {
            printf("Bueno\n");
        } else {
            if (nota == 8) {
                printf("Muy bueno\n");
            } else {
                if (nota == 9) {
                    printf("Distinguido\n");
                } else {
                    if (nota == 10) {
                        printf("Sobresaliente\n");
                    } else {
                        printf("Nota no valida.\n");
                    }
                }
            }
        }
    }
}}