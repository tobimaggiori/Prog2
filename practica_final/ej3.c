// Dada una matriz entera de 3x4, implementá las funciones suma_fila
// y suma_columna que reciban la matriz y el índice correspondiente.
#include <stdio.h>
#include <assert.h>

// suma_fila: int[][] int -> int
// Recibe una matriz y un indice i, 
// devuelve la suma de la fila i.
// entrada:
//      {{1, 2, 3, 4},
//       {5, 6, 7, 8},
//       {9, 10, 11, 12}}, 0
// salida: 10

int suma_fila(int m[3][4], int i){
    int j;
    int suma = 0;
    for(j=0;j<4;j++){
        suma = suma + m[i][j];
    }
    return suma;
}

// suma_columna: int[][] int -> int
// Recibe una matriz y un indice i, 
// devuelve la suma de la columna i.
// entrada:
//      {{1, 2, 3, 4},
//       {5, 6, 7, 8},
//       {9, 10, 11, 12}}, 0
// salida: 15
int suma_columna(int m[3][4], int j){
    int i;
    int suma = 0;
    for(i=0;i<3;i++){
        suma = suma + m[i][j];
    }
    return suma;
}


int main(){
    int m[3][4] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}
    };

    printf("Ingrese la fila de la matriz a sumar: ");
    int i;
    scanf("%d", &i);
    printf("\nLa suma de la fila %d es %d\n", i, suma_fila(m, i));

    printf("Ingrese la columna de la matriz a sumar: ");
    int j;
    scanf("%d", &j);
    printf("\nLa suma de la columna %d es %d\n", i, suma_columna(m, i));

    return 0;
}
