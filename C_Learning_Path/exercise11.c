#include <stdio.h>
#include <locale.h>

main() {
	setlocale(LC_ALL,"Turkish");
	int a,b,i,sonuc=0;
	printf("Ýlk sayý: ");
	scanf("%d",&a);
	printf("Ýkinci sayý: ");
	scanf("%d",&b);
	for(i=0;i<b;i++)
		sonuc+=a;
	printf("Sonuç= %d",sonuc);
	
}
