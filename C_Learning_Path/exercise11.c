#include <stdio.h>
#include <locale.h>

main() {
	setlocale(LC_ALL,"Turkish");
	int a,b,i,sonuc=0;
	printf("�lk say�: ");
	scanf("%d",&a);
	printf("�kinci say�: ");
	scanf("%d",&b);
	for(i=0;i<b;i++)
		sonuc+=a;
	printf("Sonu�= %d",sonuc);
	
}
