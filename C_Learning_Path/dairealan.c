#include <stdio.h>
#include <locale.h>

main() {
	setlocale(LC_ALL,"Turkish");
	float alan,cevre,pi,r;
	pi = 3.14;
	printf("Yar� �ap� girin: ");
	scanf("%f",&r);
	cevre = 2*pi*r;
	alan = pi*r*r;
	printf("Dairenin alan�= %f, dairenin �evresi= %f",alan,cevre);
}
