#include <stdio.h>
#include <locale.h>

main() {
	setlocale(LC_ALL,"Turkish");
	float alan,cevre,pi,r;
	pi = 3.14;
	printf("Yarý çapý girin: ");
	scanf("%f",&r);
	cevre = 2*pi*r;
	alan = pi*r*r;
	printf("Dairenin alaný= %f, dairenin çevresi= %f",alan,cevre);
}
