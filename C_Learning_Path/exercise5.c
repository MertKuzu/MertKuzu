#include <stdio.h>
#include <locale.h>

main() {
	setlocale(LC_ALL,"Turkish");
	int a,b,toplam=0,i=0;
	float ort;
	printf("Ka� adet say� girmek istiyorsunuz?\n");
	scanf("%d",&a);
	while(i<a){
		printf("L�tfen herhangi bir say� girin: ");
		scanf("%d",&b);
		toplam+=b;
		i++;
	}
	ort=toplam/a;
	printf("Aritmetik ortalama= %f",ort);
}
