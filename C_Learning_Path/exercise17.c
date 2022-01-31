#include <stdio.h>
#include <locale.h>

main() {
	setlocale(LC_ALL,"Turkish");
	float price,sellPrice;
	printf("Satýlan malýn fiyatý: ");
	scanf("%f",&price);
	if(price<=50) {
		sellPrice=price*1.03;
		printf("Komisyonlu satýþ fiyatý: %.2f",sellPrice);
	}
	else {
		sellPrice=price*1.02;
		printf("Komisyonlu satýþ fiyatý: %.2f",sellPrice);
	}
}
