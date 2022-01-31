#include <stdio.h>
#include <locale.h>

main() {
	setlocale(LC_ALL,"Turkish");
	int num[10],toplam=0,ort,navg[10],enkucuk;
	short int i,k,j;
	for(i=0;i<10;i++) {
		printf("Bir sayý girin: ");
		scanf("%d",&num[i]);
		toplam += num[i];
	}
	ort = toplam / 10;
	printf("Ortalama= %d\n",ort);
	for(k=0;k<10;k++){
		if(num[k]<ort)
			navg[k]=ort-num[k];
		else
			navg[k]=num[k]-ort;
		if(k==0)
			enkucuk = navg[k];
		if(navg[k]<enkucuk) {
			enkucuk = navg[k];
			j=k;
		}
	}
	printf("Ortalamaya en yakýn sayý = %d\n",num[j]);
}
