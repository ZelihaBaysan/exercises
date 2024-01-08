#include <stdio.h>
#include <stdlib.h>

int main() {
    int a[2][3] = {{1, 2, 3}, {4, 5, 6}};
    int b[2][3] = {{7, 8, 9}, {10, 11, 12}};
    int i, j;
    int c[i][j];

    printf("a\n\n");
    for (i = 0; i < 2; i++) {
        for (j = 0; j < 3; j++) {
            printf("%4d ", a[i][j]);
        }
        printf("\n");
    }

    printf("\nb\n\n");
    for (i = 0; i < 2; i++) {
        for (j = 0; j < 3; j++) {
            printf("%4d ", b[i][j]);
        }
        printf("\n");
    }

    printf("\na+b\n\n");
    for (i = 0; i < 2; i++) {
        for (j = 0; j < 3; j++) {
            c[i][j] = a[i][j] + b[i][j];
            printf("%4d ", c[i][j]);
        }
        printf("\n");
    }

    return 0;
}
