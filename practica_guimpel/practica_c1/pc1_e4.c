// Practica 1 - Ejercicio 4
// Escriba una función que determine en qué estado está el agua en función de su
// temperatura: si es negativa o 0 el estado será sólido, si positiva y menor que 100 será líquido y
// si es mayor que 100 será gaseoso. El valor de la temperatura deberá ingresarse por pantalla.
#include <stdio.h>
// Representamos la temperatura del agua mediante un numero de punto flotante que representa grados celsius.

int main(){
    int grados;
    printf("Ingresa la temperatura del agua: ");
    scanf("%f", &grados);
    if (&grados <= 0){
        printf("El estado del agua es sólido.\n");
    }
    else if (grados < 100){
        printf("El estado del agua es líquido.\n");
    }
    else {
        printf("El estado del agua es gaseoso.\n");
    }
}
