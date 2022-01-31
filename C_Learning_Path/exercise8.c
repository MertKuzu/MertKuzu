#include <stdio.h>
#include <locale.h>

main() {
	setlocale(LC_ALL,"Turkish");
	int a,b,sonuc;
	char islem;
	printf("Yapmak istediðiniz iþlemi seçin('+','-','*','/'): ");
	scanf("%c",&islem);
	printf("Ýlk sayý: ");
	scanf("%d",&a);
	printf("Ýkinci sayý: ");
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
		default: printf("Yanlýþ iþlem seçimi yaptýnýz.");
		break;
	}
	printf("Sonuç= %d",sonuc);
	
}
