#include <stdio.h>
#include <locale.h>
#include <string.h>
void rem_space(char*);

main() {
	setlocale(LC_ALL,"Turkish");
	char sentence[256];
	int letterNum;
	short int i;
	printf("Bir c�mle yaz�n�z: ");
	gets(sentence);
	rem_space(sentence);
	letterNum=strlen(sentence);
	
	
	
	printf("Girdi�iniz c�mle: %s\n",sentence);
	printf("Harf say�s�: %d",letterNum);
	
}

void rem_space(char* s) {
    char* d = s;
    do {
        while (*d == ' ') {
            ++d;
        }
    } while (*s++ = *d++);
}
