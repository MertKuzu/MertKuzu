#include <stdio.h>
#include <locale.h>
#include <stdlib.h>
#include <time.h>


main() {
	setlocale(LC_ALL,"Turkish");
	short int i,j;
	int loto[6];
	srand(time(0));
	//arraye rastgele 6-49 arasý sayý atanýyor
	for(i=0;i<6;i++) 
		loto[i]=rand()%44+6;
	for(i=0;i<6;i++) {
		for(j=i+1;j<6;j++) {
			if(loto[i]==loto[i+j]){
				loto[i]=rand()%44+6;
				i=0;
				break;
			}
			else
				continue;
		}
	}
	printf("*****SAYISAL LOTO TAHMÝNLERÝ*****\n\n");
	for(i=0;i<6;i++)
		printf("%d\t",loto[i]);
}
