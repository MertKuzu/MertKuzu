#include <iostream>
using namespace std;
int main() {
	/*if we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
	Find the sum of all the multiples of 3 or 5 below 1000.	*/	
	int i=1000,total=0;
	while(i>2) {
		if(i%3==0 && i%5==0) {
			total+=i;
			i--;
		}
		else {
			i--;
			continue;
		}
	}
	cout<<total<<endl;
	return 0;
}
