#include <stdio.h>
#include <locale.h>

main() {
	setlocale(LC_ALL,"Turkish");
	int a,b,sonuc;
	char islem;
	printf("Yapmak istedi�iniz i�lemi se�in('+','-','*','/'): ");
	scanf("%c",&islem);
	printf("�lk say�: ");
	scanf("%d",&a);
	printf("�kinci say�: ");
	scanf("%d",&b);
	switch(islem){
		case '+': sonuc=a+b;
		break;
		case '-': sonuc=a-b;
		break;
		case '*': sonuc=a*b;
		break;
		case '/': sonuc=a/b;
		break;
		default: printf("Yanl�� i�lem se�imi yapt�n�z.");
		break;
	}
	printf("Sonu�= %d",sonuc);
	
}
