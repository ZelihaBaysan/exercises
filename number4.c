#include <stdio.h>
#include <stdlib.h>
// klavyeden girilen bir cümledeki kelime sayısını bulan program
int main()
{
    char cumle[100];
    int inci = 0, sayac = 0;

    printf("lutfen bir cumle giriniz:\n");
    gets(cumle);

    while (cumle[inci])
    {
        if (cumle[inci] == 32)
        {
            sayac++;
        }
        inci++;
    }

    printf("girdiginiz cumlenin kelime sayisi %d'dir.", sayac + 1);

    return 0;
}