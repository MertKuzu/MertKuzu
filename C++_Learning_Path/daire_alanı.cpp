#include <iostream>
using namespace std;
int main() {
	setlocale(LC_ALL,"Turkish");
	float r,alan,cevre,pi;
	pi = 3.14;
	cout<<"Yar��ap girin: ";
	cin>>r;
	alan = pi*r*r;
	cevre = 2*pi*r;
	cout<<"Alan�:"<<alan<<" �evresi: "<<cevre<<endl;
}
