#include <stdio.h>
#include <locale.h>

main() {
	setlocale(LC_ALL,"Turkish");
	float price,sellPrice;
	printf("Sat�lan mal�n fiyat�: ");
	scanf("%f",&price);
	if(price<=50) {
		sellPrice=price*1.03;
		printf("Komisyonlu sat�� fiyat�: %.2f",sellPrice);
	}
	else {
		sellPrice=price*1.02;
		printf("Komisyonlu sat�� fiyat�: %.2f",sellPrice);
	}
}
