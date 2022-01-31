#include <iostream>
using namespace std;

//( >=90 :AA, 85-89:BA, 80-84:BB, 75-79:CB, 70-74:CC, 60-69:DC, <60 :FF )

int main() {
	setlocale(LC_ALL,"Turkish");
	short int vize,final;
	float ort;
	cout<<"Vize puanýnýzý girin: ";
	cin>>vize;
	cout<<"Final puanýnýzý girin: ";
	cin>>final;
	ort = ((vize*0.4)+(final*0.6));
	cout<<"Ortalamanýz: "<<ort<<endl;
	if (ort >= 90)
	cout<<"Harf notu: AA"<<endl;
	else if (ort>=85 && ort<=89)
	cout<<"Harf notu: BA"<<endl;
	else if (ort>=80 && ort<=84)
	cout<<"Harf notu: BB"<<endl;
	else if (ort>=75 && ort<=79)
	cout<<"Harf notu: CB"<<endl;
	else if (ort>=70 && ort<=74)
	cout<<"Harf notu: CC"<<endl;
	else if (ort>=60 && ort<=69)
	cout<<"Harf notu: DC"<<endl;
	else
	cout<<"Harf notu: FF"<<endl;
}
