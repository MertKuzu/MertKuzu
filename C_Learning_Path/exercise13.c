#include <stdio.h>
#include <locale.h>

main() {
	setlocale(LC_ALL,"Turkish");
	int a,b,n,win=0,lose=0,puan;
	char again;
	while(1) {
		a=rand()%100+1;
		b=rand()%100+1;
		printf("1. say�: %d\n2. say�: %d\n",a,b);
		printf("Bu say�lar�n toplam� nedir?: ");
		scanf("%d",&n);
		if(n==a+b) {
			printf("Tebrikler do�ru bildiniz.");
			win+=1;
		}
		else {
			printf("�zg�n�m yanl�� bildiniz.");
			lose+=1;
		}
		printf("Tekrar oynamak ister misiniz(e/E)? : ");
		scanf(" %c",&again);
		if(again=='e' || again=='E')
			continue;
		else
			break;
	}
	puan=(5*win)-(2*lose);
	printf("Do�ru cevap say�n�z: %d\nYanl�� cevap say�n�z: %d\nToplam puan�n�z: %d",win,lose,puan);
	
}
