
#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *archivo1;
    FILE *archivo2;
    FILE *salida;

    unsigned char caracter1, caracter2,caracter3;

    archivo1 = fopen("archivos/cancion_2.mp3","r");
    archivo2 = fopen("archivos/cosa_rara","r");
    salida = fopen("archivos/cosa2","w");

    if (archivo1 == NULL || archivo2 == NULL)
    {
        printf("\nError de apertura del archivo. \n\n");
    }
    else
    {
        long i;
        for(i=0;i<808750;i++){
   		    caracter1 = fgetc(archivo1);
   		    caracter2 = fgetc(archivo2);
   		    caracter3 = caracter1 ^ caracter2; //Aplica xor
   		    fputc(caracter3,salida); //Escribe el caracter resultante en el archivo de salida
     	}
    }

    fclose(archivo1);
    fclose(archivo2);
    fclose(salida);
    return 0;
}
