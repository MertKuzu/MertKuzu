#include <stdio.h>
#include <locale.h>

main() {
	setlocale(LC_ALL,"Turkish");
	short int i,pozitifSay,negatifSay;
	int n,pozitifToplam,negatifToplam;
	for(i=1;i<=10;i++){
		printf("%d. sayýyý girin: ",i);
		scanf("%d",&n);
		if(n>=0) {
			pozitifToplam+=n;
			pozitifSay+=1;
		}
		else {
			negatifToplam+=n;
			negatifSay+=1;
		}
	}
	printf("%d adet negatif sayý, %d adet pozitif sayý var.\nNegatif sayý toplamý= %d, Pozitif sayý toplamý= %d",negatifSay,pozitifSay,negatifToplam,pozitifToplam);
}
