#include <stdio.h>
#include <locale.h>
int asalmi(int);

main() {
	setlocale(LC_ALL,"Turkish");
	int n;
	printf("Bir say� girin: ");
	scanf("%d",&n);
	if(asalmi(n)==0) 
		printf("%d say�s� asal say� de�ildir.",n);
	else
		printf("%d say�s� asal say�d�r.",n);
}

int asalmi(int n) {
	int i;
	for(i=2;i<n;i++) {
		if(n%i==0) {
			return 0;
			break;
		}
		else 
			continue;
	}
	return 1;
}
