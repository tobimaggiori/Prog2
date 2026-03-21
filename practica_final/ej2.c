// Ejercicio 2 - Máximo de un arreglo
// Implementá una función que devuelva el valor máximo de un arreglo de enteros. Luego, escribí otra
// función que indique cuántas veces aparece ese máximo.
#include <stdio.h>

int maximo(int v[], int n) {
    int aux = 0;
    int i;

    if (n > 0) { // if para verificar que el array tiene elementos
        aux = v[0]; // el mejor caso base, empieza comparando con el primer elemento.
        for (i = 1; i < n; i++) {
            if (v[i] > aux)
                aux = v[i];
        }
    }
    return aux; 
}

int main(){
    int a[] = {2, 4, 8, 3, 5, 8, 7, 8, 6, 1, 100, 200, 500};
    int n = sizeof(a) / sizeof(a[0]); // Cantidad de enteros en el array a
    printf("El array tiene %d enteros.\n", n);
    printf("El elemento maximo del array es %d.\n", maximo(a, n));
    return 0;
}