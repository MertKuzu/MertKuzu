#include <stdio.h>
#include <locale.h>

main() {
	setlocale(LC_ALL,"Turkish");
	int sayi,sayac,muksayi;
	printf("Bir sayý girin: ");
	scanf("%d",&sayi);
	muksayi = 0;
	for(sayac=1; sayac<=sayi; sayac++){
		if(sayi%sayac==0){
			muksayi+=sayac;
		}
	}
	
	if(muksayi == sayi*2){
		printf("%d sayýsý bir mükemmel sayýdýr.\n",sayi );
	}
	else{
		printf("%d sayýsý bir mükemmel sayý deðildir.\n",sayi );
	}	
	
	
}
