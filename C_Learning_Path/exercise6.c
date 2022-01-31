#include <stdio.h>
#include <locale.h>

main() {
	setlocale(LC_ALL,"Turkish");
	int array[5000];
	int i,n;
	for(i=0;i<5000;i++) {
		n = rand()%1000+1;
		array[i] = n;
		printf("%d\n",array[i]);
	}
}
