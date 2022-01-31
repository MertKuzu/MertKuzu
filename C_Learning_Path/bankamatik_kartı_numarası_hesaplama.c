#include <stdio.h>
#include <locale.h>
void generateCardNumber();

main() {
	setlocale(LC_ALL,"Turkish");
	generateCardNumber();
}

void generateCardNumber() {
	short int j=0,k;
	unsigned long long i,cardNumber[16],number,total=0,count=0,reverseCardNumber[16];
	
	//16 haneli say�lar� tek tek kontrol ediyor
	for(i=1000000000000000;i<=9999999999999999;i++) {
		//i de�i�kenini e�er luhn algoritmas�na uygun ise yazd�r�rken kullan�ld�
		number=i;
		//basamaklar�na ay�r�p arraye tek tek ekliyor
		while(number!=0) {
			cardNumber[j]=number%10;
			number/=10;
			j++;
		}
		//array e eklenen de�erler ters oldu�undan tekrar eski haline d�nd�rmek i�in reverse
		for(k=0;k<16;k++) 
			reverseCardNumber[15-k] = cardNumber[k];
		//index numaralar�na g�re tek tek luhn algoritmas�n�n kurallar� uygulan�yor
		for(k=0;k<16;k++) {
			if(k%2==0){
				reverseCardNumber[k]*=2;
				//10dan k���kse direkt topluyor de�ilse basamakalr�na ay�r�p basamaklar� birbiriyle toplay�p toplama ekliyor
				if(reverseCardNumber[k]<10)
					total+=reverseCardNumber[k];
				else {
					number=reverseCardNumber[k];
					while(number!=0){
						total+=number%10;
						number/=10;
					}
				}
			}
			//index numaras� tek ise direkt toplama ekliyor
			else {
				total+=reverseCardNumber[k];
			}
			
		}
		if(total%10==0) {
			printf("%lld\n",i);
			//ka� tane olas� kredi kart� numaras� oldu�unu say�yor count de�i�keni
			count+=1;
			for(k=0;k<16;k++) {
				reverseCardNumber[k]="\0";
			}
			//d�ng� d�nd���nde program�n sorunsuz �al��mas� i�in s�f�rlanan de�i�kenler
			j=0;k=0;total=0;
			
		}
		else {
			for(k=0;k<16;k++) {
				//arrayleri tekrardan null de�ere d�n��t�r�yor ki sorunsuz atama yap�ls�n d�ng� d�nd���nde
				cardNumber[k]="\0";
				reverseCardNumber[k]="\0";
			}
			j=0;k=0;total=0;
			continue;
		}
				
	}	
	
	printf("\n%lld adet muhtemel kredi kart� numaras� bulunmaktad�r.",count);		
}
