#include <iostream>
using namespace std;

int main() {
	int total, i;
	for(i=5;i<=1000;i+=5) {
		if(i%7==0)
			continue;
		else
			total+=i;
	}
	cout<<"Toplam="<<total;
	return 0;
}

