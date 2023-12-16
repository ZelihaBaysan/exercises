#include <stdlib.h>
#include <stdio.h>
/*bir telefon sirketi telefonda 3 dakikaya kadar konusmanın ücretini 0.25 tl olarak belirlemiştir.
ancak sirket, konusma süresi 3 dakikayı aştığı durumda bundan sonraki her dakika için ek olarak 
0.08tl almaktadır. telefon görüşmesinin süresini dakika cinsinden girdi olarak alan ve konuşmanın 
ücretini hesaplayan bir c programı yazınız*/

int main() {
    float ucret = 0;
    int sure;
    printf("Lutfen kac dakika konusma yapmayi dusundugunuzu yaziniz:\n");
    scanf("%d", &sure);

    if (sure == 3) {
        printf("Ucret 0.25 TL'dir.\n");
    } else {
        ucret = 0.25 + (sure - 3) * 0.08;
    	printf("Ucret %f TL'dir.\n", ucret);
    }
   
    return 0;
}