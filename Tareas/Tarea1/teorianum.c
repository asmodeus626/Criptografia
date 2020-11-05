#include <stdio.h>
#include <math.h>

//Las variables x, y se utilizan para calcular la combinación lineal: mx + ny = d
int euclides(int m, int n){
    int a,b, mayor, menor, x2, y2, q;
    int x0 = 1;
    int x1 = 0;
    int y0 = 0;
    int y1 = 1;

    if(n<m){
        a = m;
        b = n;
    }else{
        a = n;
        b = m;
    }

    mayor = a;
    menor = b;
    int r=1;

    while(r > 0){
        r = a % b;
        q = a / b;
        x2 = x0 - x1*q;
        y2 = y0 - y1*q;

        //Actualización de variables para la siguiente iteración.
        a = b;
        b = r;
        x0 = x1;
        x1 = x2;
        y0 = y1;
        y1 = y2;
    }

    //printf("La combinación lineal es: %d(%d) + %d(%d) = %d\n", mayor, x0, menor, y0, a);

    if(a == 1){
        //Si el mcd es 1 significa que son primos relativos y, por lo tanto, el menor tiene
        //inverso multiplicativo módulo el mayor (que es y0).
        if(y0 < 0){
            y0 = y0 + mayor;
        }
        printf("(%d,%d)\n", menor, y0);
    }
    return a;
}

//Calcula cuántos números menores a n son sus primos relativos.
int zn_estrella(int n){
    int c = 0;
    int r;
    int i;

    for(i=1; i<n; i++){
        if(euclides(n,i) == 1){
            c++;
        }
    }
    return c;
}

void factoriza(int n){
    int i=2;

    while(n>1){
        if(n%i==0){ //Si i|n
            printf("%d,",i);
            n = n/i;
        }else{
            i++;
        }
    }
}

int main(){
    int n;
    printf("Ingrese un número para calcular Zn*\n");
    scanf("%d",&n);
    int card = zn_estrella(n);
    printf("La cardinalidad de Z%d* es: %d\n",n,card);
}
