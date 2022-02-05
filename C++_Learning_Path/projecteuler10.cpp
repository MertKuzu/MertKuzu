#include <iostream>
using namespace std;

int prime(int);

int main() {
	int i;
	unsigned int total=0;
	for(i=2;i<2000000;i++) 
		total += prime(i);
	cout<<total<<endl;
	return 0;
}

//finding prime numbers
int prime(int n) {
	int i; short int k = 1;
	for(i=2;i<n;i++) {
		if(n%i==0) {
			k=0;
			break;
		}
		else
			k=1;
	}
	if(k==0)
		return 0;
	else
		return n;
}
