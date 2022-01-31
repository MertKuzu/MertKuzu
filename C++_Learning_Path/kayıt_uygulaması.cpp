#include <iostream>
#include <locale.h>
#include <string.h>
#include <stdlib.h>
#include <conio.h>
#include <windows.h>
using namespace std;
void kayitekleme(int);
void kayitduzeltme();
void kayitsilme();
void kayitarama();
void kayitlistele();
int* isimsecme(string);
int devamEt();
int vize[128],final[128],count=0,*p,*pk;   //global varriable
string ad[128],soyad[128];
main() {
	setlocale(LC_ALL,"Turkish");
	int secim;
	while(1) {
		cout<<"=====Ana Menü=====\n1) Kayýt Ekleme\n2) Kayýt Düzeltme\n3) Kayýt Silme\n4) Kayýt Arama\n5) Kayýt Listeleme\n6) Çýkýþ\nSeçiminiz (1-5): ";
		cin>>secim;
		system("CLS");
		//anamenü her zaman ekranda olmasý için sonsuz döngü
		while(1) {
			if(secim==1) {
				//sýrasýyla kayýtlarý arraylere ekliyor her yeni ekleme yapýldýðýnda count deðiþkeni 1 artýyor.
				kayitekleme(count);
				count+=1;
				//devamEt fonksiyonunda return edilen deðer ile kýyaslama yapýlýyor
				if(devamEt()==0) {
					system("CLS");
					continue;
				}
				else {
					system("CLS");
					break;
				}		
			}
			else if(secim==2) {
				kayitduzeltme();
				if(devamEt()==0) {
					system("CLS");
					continue;
				}
				else {
					system("CLS");
					break;
				}
			}
			else if(secim==3) {
				kayitsilme();
				if(devamEt()==0) {
					system("CLS");
					continue;
				}
				else {
					system("CLS");
					break;
				}
			}
			else if(secim==4) {
				kayitarama();
				if(devamEt()==0) {
					system("CLS");
					continue;
				}
				else {
					system("CLS");
					break;
				}
			}
			else if(secim==5) {
				kayitlistele();
				//bir tuþa basana kadar listenin ekranda durmasý için
				getch();
				system("CLS");
				break;
			}
			else if(secim==6) {
				cout<<"Ýyi günler.";
				exit(1);
			}
			else {
				//hata mesajý
				system("CLS");
				cout<<"Hatalý seçim yaptýnýz lütfen tekrar seçim yapýn."<<endl;
				//3 saniye hata mesajý ekranda durduktan sonra temizlenip anamenü ekranýna dönülüyor
				Sleep(3000);
				system("CLS");
				break;
			}
		}
	}	
}
//parametre olarak yollanan index numarasýna veriler kaydediliyor
void kayitekleme(int n) {
	cout<<"Adý= ";
	cin>>ad[n];
	cout<<"Soyadý= ";
	cin>>soyad[n];
	cout<<"Vize= ";
	cin>>vize[n];
	cout<<"Final= ";
	cin>>final[n];
	system("CLS");
}
//main fonksiyonundaki return aldýðýmýz fonksiyon
int devamEt() {
	char devam;
	cout<<"Baþka iþlem yapmak istiyor musunuz? (E/H,e/h)";
	cin>>devam;
	if(devam=='E' || devam=='e') 
		return 0;
	else
		return 1;	
}
void kayitduzeltme() {
	char rusure;
	string checkad;
	cout<<"Düzelteceðiniz kiþinin adýný girin: ";
	cin>>checkad;
	while(1) {
		//isimsecme(string) fonksiyonuna girdiðimiz isim parametre olarak yollanýyor
		isimsecme(checkad);
		//*pk isimsecme(string) fonksiyonunda deðeri oluþturulan bir pointer 
		if(*pk==1)
			break;
		cout<<"Bu kaydý mý düzelteceksiniz? (E/H,e/h): ";
		cin>>rusure;
		if(rusure=='E' || rusure=='e') {
			//isimsecme(string) fonksiyonunda kaçýncý index numarasý olarak döndüyse düzelteceðimiz isim o index numarasýnýn pointerý üzerinden deðiþim yapýlýyor
			kayitekleme(*p);
			cout<<"Kayýt Düzeltildi."<<endl;
			break;
		}
		else
			break;
	}
}
void kayitsilme() {
	char devam;
	string checkad;
	cout<<"Silmek istediðiniz kiþinin adýný girin: ";
	cin>>checkad;
	while(1) {
		//isimsecme(string) fonksiyonuna girdiðimiz isim parametre olarak yollanýyor
		isimsecme(checkad);
		if(*pk==1)
			break;
		cout<<"Bu kaydý mý sileceksiniz? (E/H,e/h): ";
		cin>>devam;
		if(devam=='E' || devam=='e') {
			//isimsecme(string) fonksiyonunda kaçýncý index numarasý ise aradýðýmýz isim pointer olarak döndürülüyor ve o pointer null deðere dönüþtürülüyor
			ad[*p]="\0";
			break;
		}
		else
			break;
	}
}
void kayitarama() {
	string checkad;
	cout<<"Aradýðýnýz kiþinin adýný girin: ";
	cin>>checkad;
	//isimsecme(string) fonksiyonuna girdiðimiz isim parametre olarak yollanýyor
	isimsecme(checkad);
}
void kayitlistele() {
	short int i=0;
	cout<<"Adý ve Soyadý\t\tVize\t\tFinal\n=============\t\t=====\t\t======"<<endl;
	//kaç adet kayýt eklendiyse o kadar dönen döngü
	while(i<count) {
		//null deðerleri yazdýrmamak için kontrol
		if(ad[i]=="\0"){
			i++;
			continue;
		}
		else {
			cout<<ad[i]<<" "<<soyad[i]<<"\t\t"<<vize[i]<<"\t\t"<<final[i]<<endl;
			i++;
		}
	}
}
//fonksiyonlar içerisindeki tekrarý önlemek adýna yazdýðým baþka fonkisyon
int* isimsecme(string checkad) {
	int i,k=0;
	for(i=0;i<=count;i++) {
		//kullanýcýdan alýnan isim ile eklenmiþ olan isimleri kontrol ediyor
		if(checkad.compare(ad[i])==0) {
			cout<<"Adý ve Soyadý= "<<ad[i]<<" "<<soyad[i]<<endl<<"Vize= "<<vize[i]<<endl<<"Final= "<<final[i]<<endl;
			p=&i;
			pk=&k;
			k=0;
			return p;	
		}
		//döngü içerisinde olduðundan ve dönmeye devam ettiðinden buraya sadece k kontrol deðiþkeni atadým
		else 
			k=1;
	}
	//eðer sonuç yok ise k=1 olarak kalýyor ve kayýt bulunamadý yazdýrýyor, k deðiþkeninin pointerýný return ediyor.
	if(k==1){
		cout<<"Kayýt Bulunamadý."<<endl;
		pk=&k;
		return pk;
	}
}

