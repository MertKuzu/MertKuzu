/* The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ? */

#include <iostream>
using namespace std;

int main() {
	long long int n=600851475143,k=0,primeFactors[10];
	for(int i=2;n>=i;i++) {
		while(n%i==0) {
			primeFactors[k]=i;
			k++;
			n/=i;
		}
	}
	cout<<"The largest prime factor is= "<<primeFactors[k-1]<<endl;
	return 0;
}
