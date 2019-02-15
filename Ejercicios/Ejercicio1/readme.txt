1)
La estrategia aplicada para encontrar las claves fue la siguiente:
Abrí los archivos c1 y cancion_2 con hexedit y empecé a compararlos. Noté que algunos números se repetían con la misma frecuencia.
Por ejemplo, noté que "00" en cancion_2 se repetía con la misma frecuencia que "1c" en c1. Eso me hizo pensar que el inicio de los archivos podría ser el mismo, así que asumí que 1c correspondía a 00.

Con esto ya teníamos una de las claves(b) de la función f(i) = ai + b mod 256. Esa clave era 28(1c en hexadecimal).

Ahora solo faltaba encontrar la clave a. Para eso, observé que a FF le correspondía B7. O sea, a 255 le corresponde 183. Tenemos que:
(255*a + 28) mod 256 = 183
Para encontrar esa "a" hice un programa llamado "clavea.c" que me ayudó a encontrarla. Probando caso por caso, encontré que a=101 y así ya tenemos las 2 claves: a=101 y b=28.

Ya tenemos la función "f(i) = 101*i + 28 mod 256" que sirve para cifrar. Pero ¿para descifrar?, pues falta la función inversa. Para sacar la función inversa usé el programa "funcion.c". La función y la función inversa las guardé como un arreglo, donde a cada índice le corresponde el valor almacenado en esa casilla y las guardé en funciones.txt.

Finalmente para descifrar usé el programa "inciso1.c".

5)
Para obtener "cosa_rara" se hace lo siguiente:
-Se aplica xor de cancion1 con hola y se obtiene cosa1
-Se aplica xor de cosa1 con cancion3 y se obtiene cosa2
-Se aplica xor de cosa2 con cancion2 y se obtiene cosa_rara
