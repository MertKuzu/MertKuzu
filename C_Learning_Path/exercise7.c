#include <stdio.h>
#include <locale.h>

main() {
	setlocale(LC_ALL,"Turkish");
	int n,i,cifttop=0,ciftsayac=0,tektop=0,teksayac=0;
	float tekort,ciftort;
	for(i=1;i<=10;i++) {
		printf("%d. say�y� girin: ",i);
		scanf("%d",&n);
		if(n%2==0) {
			cifttop+=n;
			ciftsayac+=1;
		}
		else {
			tektop+=n;
			teksayac+=1;
		}
	}
	tekort=tektop/teksayac;
	ciftort=cifttop/ciftsayac;
	printf("Tek say� ortalamas�= %.1f\n�ift say� ortalamas�= %.1f",tekort,ciftort);
}
