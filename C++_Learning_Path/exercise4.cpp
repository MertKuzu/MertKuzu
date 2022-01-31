/*A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers. */
#include <iostream>
using namespace std;
int palindrome(int);
void largestPalindrome(int);
int largest;  //largest palindrome varriable
int main() {
	int i,k,j;
	//this loops are calculate 3-digit multiply
	for(i=100;i<1000;i++) { 
		for(k=i;k<1000;k++) {
			j=palindrome(i*k);   //j is palindrome return value
			largestPalindrome(j);  
		}
	}
	cout<<"The largest palindrome number is "<<largest<<endl;
	return 0;
}
int palindrome(int num) {
	int i,palindrome=0;
	i=num;
	while(i!=0) {
		palindrome*=10;   //swiping 1 digit to left
		palindrome+=i%10;  //digit calculator
		i/=10;        
	}
	if(num==palindrome) 
		return num;    //if num is palindrome then return num
	else
		return 0;
}
void largestPalindrome(int num) {
	if(num>largest)    //largest palindrome calculator func
		largest=num;
}
