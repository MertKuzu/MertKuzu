#include <stdio.h>
#include <locale.h>
#include <string.h>


main() {
	setlocale(LC_ALL,"Turkish");
	char araba[8];
	short int i;
	float time,taksiprice=5,ticariprice=6.5,minibusprice=6;
	while(1) {
		printf("Ara� tipinizi belirtin (taksi/minib�s/ticari): ");
		scanf("%s",&araba);
		if(strcmp(araba,"taksi")==0 || strcmp(araba,"minibus")==0 || strcmp(araba,"ticari")==0)
			break;
		else {
			printf("Hatal� ara� tipi belirttiniz. L�tfen tekrar belirtin.\n");
			continue;
		}
	}
	if(strcmp(araba,"taksi")==0) {
		printf("Ka� saat park ettiniz: ");
		scanf("%f",&time);
		for(i=1;i<=time;i++) 
			taksiprice*=1.2;	
		printf("Park �creti= %f",taksiprice);
	}
	
	else if(strcmp(araba,"ticari")==0) {
		printf("Ka� saat park ettiniz: ");
		scanf("%f",&time);
		for(i=1;i<=time;i++)
			ticariprice*=1.25;
		printf("Park �creti= %f",ticariprice);
	}
	
	else {
		printf("Ka� saat park ettiniz: ");
		scanf("%f",&time);
		for(i=1;i<=time;i++)
			minibusprice*=1.215;
		printf("Park �creti= %f",minibusprice);
	}
}

