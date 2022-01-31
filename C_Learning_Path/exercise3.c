#include <stdio.h>
#include <locale.h>

main() {
	setlocale(LC_ALL,"Turkish");
	int a,i;
	char asalmi=0;
	printf("Bir sayý girin: ");
	scanf("%d",&a);
	for(i=2;i<a;i++){
		if(a%i==0)
			break;
		else
			asalmi=1;
	}
	
	if(asalmi==1)
		printf("%d sayýsý asaldýr.",a);
	else
		printf("%d sayýsý asal deðildir",a);
}
