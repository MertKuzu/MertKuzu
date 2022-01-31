#include <stdio.h>
#include <locale.h>


main() {
	setlocale(LC_ALL,"Turkish");
	char aylar[8];
	int sicaklik[32],total=0;
	float ort;
	//eki = en küçük indis, ek = en küçük 
	short int i,eki=1,ek=100;
	printf("Hangi ayýn sýcaklýk bilgilerini gireceksiniz: ");
	scanf("%s",&aylar);
	if(strcmp(aylar,"ocak")==0 || strcmp(aylar,"mart")==0 || strcmp(aylar,"mayis")==0 || strcmp(aylar,"temmuz")==0 || strcmp(aylar,"agustos")==0 || strcmp(aylar,"ekim")==0 || strcmp(aylar,"aralik")==0) {
		for(i=1;i<=31;i++) {
			printf("%d. gün hava sýcaklýðý: ",i);
			scanf("%d",&sicaklik[i]);
			if(sicaklik[i]<ek) {
				//en düþük sýcaklýðý deðiþkene atýyor
				ek = sicaklik[i];
				//en düþük sýcaklýðýn kaçýncý gün olduðunu deðiþkene atýyor
				eki = i;
			}
			total+=sicaklik[i];
		}
		ort = total/31;
		printf("%s ayýnýn ortalama sýcaklýðý: %.2f derece, en düþük sýcaklýðý: %d. gün %d derece",aylar,ort,eki,ek);
	}
	else if(strcmp(aylar,"nisan")==0 || strcmp(aylar,"haziran")==0 || strcmp(aylar,"eylul")==0 || strcmp(aylar,"kasim")==0) {
		for(i=1;i<=30;i++) {
			printf("%d. gün hava sýcaklýðý: ",i);
			scanf("%d",&sicaklik[i]);
			if(sicaklik[i]<ek) {
				//en düþük sýcaklýðý deðiþkene atýyor
				ek = sicaklik[i];
				//en düþük sýcaklýðýn kaçýncý gün olduðunu deðiþkene atýyor
				eki = i;
			}
			total+=sicaklik[i];
		}
		ort = total/30;
		printf("%s ayýnýn ortalama sýcaklýðý: %.2f derece, en düþük sýcaklýðý: %d. gün %d derece",aylar,ort,eki,ek);	
	}
	else if(strcmp(aylar,"subat")==0) {
		for(i=1;i<=28;i++) {
			printf("%d. gün hava sýcaklýðý: ",i);
			scanf("%d",&sicaklik[i]);
			if(sicaklik[i]<ek) {
				//en düþük sýcaklýðý deðiþkene atýyor
				ek = sicaklik[i];
				//en düþük sýcaklýðýn kaçýncý gün olduðunu deðiþkene atýyor
				eki = i;
			}
			total+=sicaklik[i];
		}
		ort = total/28;
		printf("%s ayýnýn ortalama sýcaklýðý: %.2f derece, en düþük sýcaklýðý: %d. gün %d derece",aylar,ort,eki,ek);	
	}
	
	else
		printf("Yanlýþ bir ay adý girdiniz.");
	
}


