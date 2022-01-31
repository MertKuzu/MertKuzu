#include <stdio.h>
#include <locale.h>

main() {
	setlocale(LC_ALL,"Turkish");
	int a,b,n,win=0,lose=0,puan;
	char again;
	while(1) {
		a=rand()%100+1;
		b=rand()%100+1;
		printf("1. sayý: %d\n2. sayý: %d\n",a,b);
		printf("Bu sayýlarýn toplamý nedir?: ");
		scanf("%d",&n);
		if(n==a+b) {
			printf("Tebrikler doðru bildiniz.");
			win+=1;
		}
		else {
			printf("Üzgünüm yanlýþ bildiniz.");
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
	printf("Doðru cevap sayýnýz: %d\nYanlýþ cevap sayýnýz: %d\nToplam puanýnýz: %d",win,lose,puan);
	
}
