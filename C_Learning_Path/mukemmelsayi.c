#include <stdio.h>
#include <locale.h>

main() {
	setlocale(LC_ALL,"Turkish");
	int sayi,sayac,muksayi;
	printf("Bir say� girin: ");
	scanf("%d",&sayi);
	muksayi = 0;
	for(sayac=1; sayac<=sayi; sayac++){
		if(sayi%sayac==0){
			muksayi+=sayac;
		}
	}
	
	if(muksayi == sayi*2){
		printf("%d say�s� bir m�kemmel say�d�r.\n",sayi );
	}
	else{
		printf("%d say�s� bir m�kemmel say� de�ildir.\n",sayi );
	}	
	
	
}
