#include <stdio.h>
#include <locale.h>

main() {
	setlocale(LC_ALL,"Turkish");
	int a,i;
	char asalmi=0;
	printf("Bir say� girin: ");
	scanf("%d",&a);
	for(i=2;i<a;i++){
		if(a%i==0)
			break;
		else
			asalmi=1;
	}
	
	if(asalmi==1)
		printf("%d say�s� asald�r.",a);
	else
		printf("%d say�s� asal de�ildir",a);
}
