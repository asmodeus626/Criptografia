
//En esta clase se realizan operaciones con matrices cuadradas.

public class OperMat{

    //Calcula i módulo n. Siempre devuelve un número positivo.
    public static int modPositivo(int i, int n){
        int res = i%n;
        if(res < 0)
            res+=n;

        return res;
    }

    //Calcula la transpuesta de una matriz.
    public static int[][] transpuesta(int[][] matriz){
        int[][] matrizT = new int[matriz.length][matriz.length];
        for(int i=0;i<matriz.length;i++){
            for(int j=0;j<matriz.length;j++){
                matrizT[j][i] = matriz[i][j];
            }
        }
        return matrizT;
    }

    //Calcula la determinante de una matriz (se supone que es cuadrada).
    public static int det(int[][] matriz){
        if(matriz.length == 1){
            return matriz[0][0];
        }
        

    }

    public static void main(String[] args){
        int residuo = -27 % 26;
        System.out.println(residuo);
    }
}