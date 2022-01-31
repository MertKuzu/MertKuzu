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
	
	//16 haneli sayýlarý tek tek kontrol ediyor
	for(i=1000000000000000;i<=9999999999999999;i++) {
		//i deðiþkenini eðer luhn algoritmasýna uygun ise yazdýrýrken kullanýldý
		number=i;
		//basamaklarýna ayýrýp arraye tek tek ekliyor
		while(number!=0) {
			cardNumber[j]=number%10;
			number/=10;
			j++;
		}
		//array e eklenen deðerler ters olduðundan tekrar eski haline döndürmek için reverse
		for(k=0;k<16;k++) 
			reverseCardNumber[15-k] = cardNumber[k];
		//index numaralarýna göre tek tek luhn algoritmasýnýn kurallarý uygulanýyor
		for(k=0;k<16;k++) {
			if(k%2==0){
				reverseCardNumber[k]*=2;
				//10dan küçükse direkt topluyor deðilse basamakalrýna ayýrýp basamaklarý birbiriyle toplayýp toplama ekliyor
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
			//index numarasý tek ise direkt toplama ekliyor
			else {
				total+=reverseCardNumber[k];
			}
			
		}
		if(total%10==0) {
			printf("%lld\n",i);
			//kaç tane olasý kredi kartý numarasý olduðunu sayýyor count deðiþkeni
			count+=1;
			for(k=0;k<16;k++) {
				reverseCardNumber[k]="\0";
			}
			//döngü döndüðünde programýn sorunsuz çalýþmasý için sýfýrlanan deðiþkenler
			j=0;k=0;total=0;
			
		}
		else {
			for(k=0;k<16;k++) {
				//arrayleri tekrardan null deðere dönüþtürüyor ki sorunsuz atama yapýlsýn döngü döndüðünde
				cardNumber[k]="\0";
				reverseCardNumber[k]="\0";
			}
			j=0;k=0;total=0;
			continue;
		}
				
	}	
	
	printf("\n%lld adet muhtemel kredi kartý numarasý bulunmaktadýr.",count);		
}
