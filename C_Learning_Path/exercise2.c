#include <stdio.h>
#include <locale.h>

main() {
	setlocale(LC_ALL,"Turkish");
	int a,b,toplam=0;
	printf("Ýlk sayýyý girin: ");
	scanf("%d",&a);
	printf("Ýkinci sayýyý girin: ");
	scanf("%d",&b);
	for(;a<b;a++){
		if(a%2==0)
			toplam+=a;
		else
			continue;
	}
	printf("Toplam= %d",toplam);
}
