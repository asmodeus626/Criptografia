#include <stdio.h>
#include <stdlib.h>

int main()
{

	unsigned char hola[] = "hola";
	unsigned char caracter1, caracter2,caracter3;
	FILE *cancion1;
	FILE *cosa1;
	cancion1 = fopen("archivos/cancion_1.mp3","r");
	cosa1 = fopen("archivos/cosa1","w");

	if (cancion1 == NULL)
    {
        printf("\nError de apertura del archivo. \n\n");
    }
    else
    {
        long i;
        for(i=0;i<808750;i++){
   		    caracter1 = fgetc(cancion1);
   		    caracter2 = hola[i%4];
   		    caracter3 = caracter1 ^ caracter2; //Aplica xor
   		    fputc(caracter3,cosa1); //Escribe el caracter resultante en el archivo de salida
     	}
  }

	fclose(cancion1);
	fclose(cosa1);
}
