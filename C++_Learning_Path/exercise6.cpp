#include <iostream>
using namespace std;
int sumsquare(void);   //calculate sum of the square
int squaresum(void);	//caluclate square of the sum
int main() {
	int n,m,result;
	n=sumsquare();     
	m=squaresum();
	if(n<m)
		result=m-n;
	else
		result=n-m;
	cout<<"Result is "<<result<<endl;
	return 0;
}
int sumsquare(void) {
	short int i;
	int total=0;
	for(i=1;i<=100;i++) 
		total+=i*i;     
	return total;
}
int squaresum(void) {
	short int i;
	int total=0;
	for(i=1;i<=100;i++)
		total+=i;
	total=total*total;
	return total;
}
