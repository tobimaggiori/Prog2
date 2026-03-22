#include <stdio.h>
// Este programa suma todos los elementos de una matriz de dos maneras:
// una sumando todas sus filas y las otras sumando todas sus columnas.

int suma_filas(int f, int c, int m[f][c]){
    int i, j;
    int suma = 0;
    for(i=0; i<f; i++){
        for(j=0; j<c; j++){
            suma = suma + m[i][j];
        }
    }
    return suma;
}

int suma_columnas(int f, int c, int m[f][c]){
    int i, j;
    int suma = 0;
    for(j=0; j<c; j++){
        for(i=0; i<f; i++){
            suma = suma + m[i][j];
        }
    }
    return suma;    
}

int main(){
    int m[3][4] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}
    };
    // int total = sizeof(m);  Tamaño total de la matriz en bytes
    int filas = sizeof(m) / sizeof(m[0]); // Tamaño total / Tamaño de su primer fila = cantidad de filas
    int columnas = sizeof(m[0]) / sizeof(m[0][0]); // Tamaño de una fila / tamaño de un elemento = cantidad de columnas
    printf("La matriz dada es de %dx%d, \n", filas, columnas);
    printf("la suma de sus filas es %d y \n", suma_filas(filas, columnas, m));
    printf("la suma de sus columnas es %d\n", suma_columnas(filas, columnas, m));
    return 0;
}
