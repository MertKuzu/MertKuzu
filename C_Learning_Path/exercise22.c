#include <stdio.h>
#include <locale.h>
#include <string.h>
void rem_space(char*);

main() {
	setlocale(LC_ALL,"Turkish");
	char sentence[256];
	int letterNum;
	short int i;
	printf("Bir cümle yazýnýz: ");
	gets(sentence);
	rem_space(sentence);
	letterNum=strlen(sentence);
	
	
	
	printf("Girdiðiniz cümle: %s\n",sentence);
	printf("Harf sayýsý: %d",letterNum);
	
}

void rem_space(char* s) {
    char* d = s;
    do {
        while (*d == ' ') {
            ++d;
        }
    } while (*s++ = *d++);
}
