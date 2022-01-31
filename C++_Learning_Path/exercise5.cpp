#include <iostream>
using namespace std;
int smallest(int);
int main() {
	int i,k;
	for(i=20;;i++) {   //20 to infinite because trying to all numbers 
		k=smallest(i);    //k is func return 
		if(k==0)
			break;       //when the program find the smallest division number, program will stop.
		else
			continue;
	}
	return 0;
}
int smallest(int num) {
	short int i,k=0;      //k is control varriable
	for(i=1;i<=20;i++) {
		if(num%i==0)          //division [1,20] numbers
			k=0;    
		else {
			k=1;     
			break;
		}
	}
	if(k==0) {
		cout<<num<<endl;
		return 0;
	}
	else
		return 1;
}
