#include <stdio.h>
#include <locale.h>
main() {
	setlocale(LC_ALL,"Turkish");
	int n, i=0;
	char name[20],surname[20];
	printf("�sminiz: ");
	scanf("%s",&name);
	printf("Soyad�n�z: ");
	scanf("%s",&surname);
	printf("Ka� kez isminizi yazd�rmak istiyorsunuz: ");
	scanf("%d",&n);
	while(i<n) {
		printf("%s %s\n",name,surname);
		i++;
	}
}
