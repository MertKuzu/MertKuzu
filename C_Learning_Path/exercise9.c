#include <stdio.h>
#include <locale.h>
#include <math.h>

main() {
	setlocale(LC_ALL,"Turkish");
	int taban,us,sonuc;
	printf("Taban say�y� girin: ");
	scanf("%d",&taban);
	printf("�ss� girin: ");
	scanf("%d",&us);
	sonuc=pow(taban,us);
	printf("Sonu�= %d",sonuc);
}
