#include <stdio.h>
#include <conio.h>

int main() {
	int a,b,toplam;
	printf("Toplamak istediginiz iki sayi girin:");
	scanf("%d%d",&a,&b);
	toplam = a+b;
	printf("Toplam=%d",toplam);
	getch();
}
