#include <stdio.h>
#include <locale.h>

main() {
	setlocale(LC_ALL,"Turkish");
	short int i=1,sayac=0;
	int n,toplam=0;
	do {
		printf("%d. sayýyý girin: ",i);
		scanf("%d",&n);
		if(n<100)
			toplam+=n;
		else if(n<200 && n>100)
			sayac+=1;
		else {
			if(n%4==0)
				printf("%d\n",n);
		}
		i++;
	}
	while(i<=10);

	printf("100 den küçük toplam= %d, 100-200 sayý adedi= %d",toplam,sayac);
}
