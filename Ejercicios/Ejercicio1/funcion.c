
#include <stdio.h>

int main()
{
	int i;
	int funcion[256];
	int inversa[256];
	for(i=0;i<256;i++)
	{
		funcion[i]=(i*101 + 28) % 256;
	}

	for(i=0;i<256;i++)
	{
		inversa[funcion[i]]=i;
	}

	printf("función:\n");
	for(i=0;i<256;i++)
	{
		printf("%d, ",funcion[i]);
	}

	printf("\nfunción inversa:\n");
	for(i=0;i<256;i++)
	{
		printf("%d, ",inversa[i]);
	}
	printf("\n");
}
