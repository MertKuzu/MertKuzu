#include <iostream>
using namespace std;
int main() {
	setlocale(LC_ALL,"Turkish");
	float r,alan,cevre,pi;
	pi = 3.14;
	cout<<"Yarýçap girin: ";
	cin>>r;
	alan = pi*r*r;
	cevre = 2*pi*r;
	cout<<"Alaný:"<<alan<<" Çevresi: "<<cevre<<endl;
}
