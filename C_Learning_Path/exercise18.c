#include <stdio.h>
#include <locale.h>

main() {
	setlocale(LC_ALL,"Turkish");
	int n,i,total=0;
	printf("Bir say� girin: ");
	scanf("%d",&n);
	for(i=1;i<n;i++) {
		if(n%i==0)
			total+=i;
	}
	if(total==n)
		printf("%d say�s� bir m�kemmel say�d�r.",n);
	else
		printf("%d say�s� bir m�kemmel say� de�ildir.",n);
}
