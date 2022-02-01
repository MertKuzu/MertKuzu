#include <iostream>
using namespace std;
int prime_number(int);

int main() {
	int i,k=0; short int n;
	for(i=2;;i++) {
		n = prime_number(i);
		if(n==1)        //prime number counter
			k += 1;
		if(k==10001) {
			cout<<"10001st prime number is "<<i<<endl;
			break;
		}
	}
}

int prime_number(int num) {
	int i; short int k=1;
	for(i=2;i<num;i++) {
		if(num%i==0) {
			k=0;
			break;
		}
		else 
			k=1;
	}
	return k;
}
