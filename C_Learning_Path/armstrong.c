#include <stdio.h>
#include <locale.h>


int main() {
	setlocale(LC_ALL,"Turkish");
	int i,sayi,modsayi,sonuc;
	
	
	for(i=100;i<=999;i++) {
		sonuc=0;
		sayi = i;
		while (sayi != 0) {
			modsayi = sayi%10;
			sonuc += modsayi*modsayi*modsayi;
			sayi /= 10;
		}
		if (i == sonuc)
			printf("%d sayýsý armstrong sayýsýdýr.\n",i);
		else
			continue;
	}
	
}
