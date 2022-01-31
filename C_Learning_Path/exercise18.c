#include <stdio.h>
#include <locale.h>

main() {
	setlocale(LC_ALL,"Turkish");
	int n,i,total=0;
	printf("Bir sayý girin: ");
	scanf("%d",&n);
	for(i=1;i<n;i++) {
		if(n%i==0)
			total+=i;
	}
	if(total==n)
		printf("%d sayýsý bir mükemmel sayýdýr.",n);
	else
		printf("%d sayýsý bir mükemmel sayý deðildir.",n);
}
