#include <stdio.h>
#include <locale.h>

main() {
	setlocale(LC_ALL,"Turkish");
	short int i,j,l;
	int a[3][2],b[2][4],c[3][4],total;
	for(i=0;i<3;i++) {
		for(j=0;j<2;j++) {
			printf("A matrisin Elemanlarýný girin: ");
			scanf("%d",&a[i][j]);
		}
	}
	
	for(i=0;i<2;i++) {
		for(j=0;j<4;j++) {
			printf("B matrisinin elemanlarýný girin: ");
			scanf("%d",&b[i][j]);
		}
	}

	for(i=0;i<3;i++) {
		for(l=0;l<4;l++) {
			for(j=0;j<2;j++) {
				total+=a[i][j]*b[j][l];
			}
			c[i][l]=total;
			total=0;
		}
	}
	printf("------A*B=C MATRÝSÝ-----\n\n");
	for(i=0;i<3;i++) {
		for(j=0;j<4;j++) 
			printf("%d\t",c[i][j]);	
		printf("\n");	
	}
}
