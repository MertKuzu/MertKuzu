#include <stdio.h>
#include <locale.h>
#include <math.h>

main() {
	setlocale(LC_ALL,"Turkish");
	int taban,us,sonuc;
	printf("Taban sayýyý girin: ");
	scanf("%d",&taban);
	printf("Üssü girin: ");
	scanf("%d",&us);
	sonuc=pow(taban,us);
	printf("Sonuç= %d",sonuc);
}
