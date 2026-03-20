// Escribí una función float promedio(int v[], int n) que reciba un arreglo de enteros y su
// tamaño, y devuelva el promedio aritmético de sus elementos.

#include <stdio.h>

float promedio(int v[], int n){
    int i;
    int suma = 0;
    for(i=0; i<n; i++){
        suma = v[i] + suma;
    }
    return (float)suma / n;
}

int main(){
    int a[] = {5, 5, 10, 10};
    int n = sizeof(a) / sizeof(a[0]); // Con esto obtenemos la cantidad de enteros que tiene un array de enteros.
    printf("El array ocupa %d bytes y cada uno de sus elementos ocupa %d bytes. \n", sizeof(a), sizeof(a[0]));
    printf("Por lo tanto, el array tiene %d elementos.\n", n);
    printf("Luego, el promedio del array es %.2f\n", promedio(a, n));
}