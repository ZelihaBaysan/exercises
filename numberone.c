#include <stdlib.h>
#include <stdio.h>
/*bir üçgenin açılarını girdi oalrak alan ve bu üçgenin eşit kenar, ikiz kenar
veya çeşit kenar üçgen olup olmadığını belirleyen bir c programı yazınız.
açıların üçgen oluşturup oluşturmadığını mutlaka kontrol ediniz.*/
int main() {
    int aci1 = 0, aci2 = 0, aci3 = 0;

    printf("Lutfen 3 adet aci degeri giriniz:\n");
    scanf("%d %d %d", &aci1, &aci2, &aci3);

    if (aci1 + aci2 + aci3 == 180) {
        if (aci1 == aci2 && aci1 == aci3) {
            printf("Ucgeniniz eskenar ucgendir.\n");
        } else if (aci1 == aci2 || aci1 == aci3 || aci2 == aci3) {
            printf("Ucgeniniz ikizkenar ucgendir.\n");
        } else {
            printf("Ucgeniniz cesitkenar ucgendir.\n");
        }
    } else {
        printf("Girdiginiz acilar bir ucgen olusturmuyor.\n");
    }

    return 0;
}