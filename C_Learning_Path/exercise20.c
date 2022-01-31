#include <stdio.h>
#include <locale.h>


main() {
	setlocale(LC_ALL,"Turkish");
	int vize,final,ort[10],hold;
	short int i,j;
	for(i=0;i<10;i++) {
		printf("%d. vize notunu girin: ",i+1);
		scanf("%d",&vize);
		printf("%d. final notunu girin: ",i+1);
		scanf("%d",&final);
		ort[i]=(vize*0.4)+(final*0.6);
	}
	for(i=0;i<9;i++) {
		for(j=i+1;j<10;j++) {
			if(ort[i]>ort[j]) {
				hold = ort[i];
				ort[i]=ort[j];
				ort[j] = hold;
			}
		}
	}
	
	printf("********Sýralanmýþ Ortalamalar********");
	for(i=0;i<10;i++)
		printf("\n%d",ort[i]);
	
}
