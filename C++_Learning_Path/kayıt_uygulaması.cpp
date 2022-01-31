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
		cout<<"=====Ana Men�=====\n1) Kay�t Ekleme\n2) Kay�t D�zeltme\n3) Kay�t Silme\n4) Kay�t Arama\n5) Kay�t Listeleme\n6) ��k��\nSe�iminiz (1-5): ";
		cin>>secim;
		system("CLS");
		//anamen� her zaman ekranda olmas� i�in sonsuz d�ng�
		while(1) {
			if(secim==1) {
				//s�ras�yla kay�tlar� arraylere ekliyor her yeni ekleme yap�ld���nda count de�i�keni 1 art�yor.
				kayitekleme(count);
				count+=1;
				//devamEt fonksiyonunda return edilen de�er ile k�yaslama yap�l�yor
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
				//bir tu�a basana kadar listenin ekranda durmas� i�in
				getch();
				system("CLS");
				break;
			}
			else if(secim==6) {
				cout<<"�yi g�nler.";
				exit(1);
			}
			else {
				//hata mesaj�
				system("CLS");
				cout<<"Hatal� se�im yapt�n�z l�tfen tekrar se�im yap�n."<<endl;
				//3 saniye hata mesaj� ekranda durduktan sonra temizlenip anamen� ekran�na d�n�l�yor
				Sleep(3000);
				system("CLS");
				break;
			}
		}
	}	
}
//parametre olarak yollanan index numaras�na veriler kaydediliyor
void kayitekleme(int n) {
	cout<<"Ad�= ";
	cin>>ad[n];
	cout<<"Soyad�= ";
	cin>>soyad[n];
	cout<<"Vize= ";
	cin>>vize[n];
	cout<<"Final= ";
	cin>>final[n];
	system("CLS");
}
//main fonksiyonundaki return ald���m�z fonksiyon
int devamEt() {
	char devam;
	cout<<"Ba�ka i�lem yapmak istiyor musunuz? (E/H,e/h)";
	cin>>devam;
	if(devam=='E' || devam=='e') 
		return 0;
	else
		return 1;	
}
void kayitduzeltme() {
	char rusure;
	string checkad;
	cout<<"D�zeltece�iniz ki�inin ad�n� girin: ";
	cin>>checkad;
	while(1) {
		//isimsecme(string) fonksiyonuna girdi�imiz isim parametre olarak yollan�yor
		isimsecme(checkad);
		//*pk isimsecme(string) fonksiyonunda de�eri olu�turulan bir pointer 
		if(*pk==1)
			break;
		cout<<"Bu kayd� m� d�zelteceksiniz? (E/H,e/h): ";
		cin>>rusure;
		if(rusure=='E' || rusure=='e') {
			//isimsecme(string) fonksiyonunda ka��nc� index numaras� olarak d�nd�yse d�zeltece�imiz isim o index numaras�n�n pointer� �zerinden de�i�im yap�l�yor
			kayitekleme(*p);
			cout<<"Kay�t D�zeltildi."<<endl;
			break;
		}
		else
			break;
	}
}
void kayitsilme() {
	char devam;
	string checkad;
	cout<<"Silmek istedi�iniz ki�inin ad�n� girin: ";
	cin>>checkad;
	while(1) {
		//isimsecme(string) fonksiyonuna girdi�imiz isim parametre olarak yollan�yor
		isimsecme(checkad);
		if(*pk==1)
			break;
		cout<<"Bu kayd� m� sileceksiniz? (E/H,e/h): ";
		cin>>devam;
		if(devam=='E' || devam=='e') {
			//isimsecme(string) fonksiyonunda ka��nc� index numaras� ise arad���m�z isim pointer olarak d�nd�r�l�yor ve o pointer null de�ere d�n��t�r�l�yor
			ad[*p]="\0";
			break;
		}
		else
			break;
	}
}
void kayitarama() {
	string checkad;
	cout<<"Arad���n�z ki�inin ad�n� girin: ";
	cin>>checkad;
	//isimsecme(string) fonksiyonuna girdi�imiz isim parametre olarak yollan�yor
	isimsecme(checkad);
}
void kayitlistele() {
	short int i=0;
	cout<<"Ad� ve Soyad�\t\tVize\t\tFinal\n=============\t\t=====\t\t======"<<endl;
	//ka� adet kay�t eklendiyse o kadar d�nen d�ng�
	while(i<count) {
		//null de�erleri yazd�rmamak i�in kontrol
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
//fonksiyonlar i�erisindeki tekrar� �nlemek ad�na yazd���m ba�ka fonkisyon
int* isimsecme(string checkad) {
	int i,k=0;
	for(i=0;i<=count;i++) {
		//kullan�c�dan al�nan isim ile eklenmi� olan isimleri kontrol ediyor
		if(checkad.compare(ad[i])==0) {
			cout<<"Ad� ve Soyad�= "<<ad[i]<<" "<<soyad[i]<<endl<<"Vize= "<<vize[i]<<endl<<"Final= "<<final[i]<<endl;
			p=&i;
			pk=&k;
			k=0;
			return p;	
		}
		//d�ng� i�erisinde oldu�undan ve d�nmeye devam etti�inden buraya sadece k kontrol de�i�keni atad�m
		else 
			k=1;
	}
	//e�er sonu� yok ise k=1 olarak kal�yor ve kay�t bulunamad� yazd�r�yor, k de�i�keninin pointer�n� return ediyor.
	if(k==1){
		cout<<"Kay�t Bulunamad�."<<endl;
		pk=&k;
		return pk;
	}
}

