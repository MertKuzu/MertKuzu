#include <stdio.h>
#include <locale.h>


main() {
	setlocale(LC_ALL,"Turkish");
	char aylar[8];
	int sicaklik[32],total=0;
	float ort;
	//eki = en k���k indis, ek = en k���k 
	short int i,eki=1,ek=100;
	printf("Hangi ay�n s�cakl�k bilgilerini gireceksiniz: ");
	scanf("%s",&aylar);
	if(strcmp(aylar,"ocak")==0 || strcmp(aylar,"mart")==0 || strcmp(aylar,"mayis")==0 || strcmp(aylar,"temmuz")==0 || strcmp(aylar,"agustos")==0 || strcmp(aylar,"ekim")==0 || strcmp(aylar,"aralik")==0) {
		for(i=1;i<=31;i++) {
			printf("%d. g�n hava s�cakl���: ",i);
			scanf("%d",&sicaklik[i]);
			if(sicaklik[i]<ek) {
				//en d���k s�cakl��� de�i�kene at�yor
				ek = sicaklik[i];
				//en d���k s�cakl���n ka��nc� g�n oldu�unu de�i�kene at�yor
				eki = i;
			}
			total+=sicaklik[i];
		}
		ort = total/31;
		printf("%s ay�n�n ortalama s�cakl���: %.2f derece, en d���k s�cakl���: %d. g�n %d derece",aylar,ort,eki,ek);
	}
	else if(strcmp(aylar,"nisan")==0 || strcmp(aylar,"haziran")==0 || strcmp(aylar,"eylul")==0 || strcmp(aylar,"kasim")==0) {
		for(i=1;i<=30;i++) {
			printf("%d. g�n hava s�cakl���: ",i);
			scanf("%d",&sicaklik[i]);
			if(sicaklik[i]<ek) {
				//en d���k s�cakl��� de�i�kene at�yor
				ek = sicaklik[i];
				//en d���k s�cakl���n ka��nc� g�n oldu�unu de�i�kene at�yor
				eki = i;
			}
			total+=sicaklik[i];
		}
		ort = total/30;
		printf("%s ay�n�n ortalama s�cakl���: %.2f derece, en d���k s�cakl���: %d. g�n %d derece",aylar,ort,eki,ek);	
	}
	else if(strcmp(aylar,"subat")==0) {
		for(i=1;i<=28;i++) {
			printf("%d. g�n hava s�cakl���: ",i);
			scanf("%d",&sicaklik[i]);
			if(sicaklik[i]<ek) {
				//en d���k s�cakl��� de�i�kene at�yor
				ek = sicaklik[i];
				//en d���k s�cakl���n ka��nc� g�n oldu�unu de�i�kene at�yor
				eki = i;
			}
			total+=sicaklik[i];
		}
		ort = total/28;
		printf("%s ay�n�n ortalama s�cakl���: %.2f derece, en d���k s�cakl���: %d. g�n %d derece",aylar,ort,eki,ek);	
	}
	
	else
		printf("Yanl�� bir ay ad� girdiniz.");
	
}


