#include <stdio.h>
#include <locale.h>
main() {
	setlocale(LC_ALL,"Turkish");
	int n, i=0;
	char name[20],surname[20];
	printf("Ýsminiz: ");
	scanf("%s",&name);
	printf("Soyadýnýz: ");
	scanf("%s",&surname);
	printf("Kaç kez isminizi yazdýrmak istiyorsunuz: ");
	scanf("%d",&n);
	while(i<n) {
		printf("%s %s\n",name,surname);
		i++;
	}
}
