#include <stdio.h>
#include <string.h>

int main() {
    char cumle[100];
    int i;

    printf("Cumle giriniz: ");
    gets(cumle);

    for (i = strlen(cumle) - 1; i >= 0; i--) {
        printf("%c", cumle[i]);
    }

    return 0;
}
