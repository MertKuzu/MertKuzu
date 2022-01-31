#include <stdio.h>
#include <locale.h>
#include <string.h>

main() {
	setlocale(LC_ALL,"Turkish");
	char word[10],reword[10];
	int i,j=0,a=0;
	printf("Bir kelime girin: ");
	gets(word);
	int lenght = strlen(word);
	for(i=lenght-1;i>=0;i--) {
		reword[j] = word[i];
		j++;
	}
	for(i=0;i<lenght;i++) {
		if(reword[a]==word[i])
			a++;
	}
	
	if(a==lenght)
		printf("%s kelimesi bir palindrome kelimedir.",word);
	else
		printf("%s kelimesi bir palindrome kelime deðildir.",word);
}
