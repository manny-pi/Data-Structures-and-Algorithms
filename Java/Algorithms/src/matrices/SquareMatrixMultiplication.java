package matrices;

import java.util.Arrays; 


public class SquareMatrixMultiplication {

    public static int[][] squareMatrixMultiply(int[][] A, int[][] B) {

        int n = A.length; // n equals the number of rows in A
        int[][] c = new int[n][n]; 

        for(int i = 0; i < n; i++) { 
            for(int j = 0; j < n; j++) {
                for(int k = 0; k < n; k++) { 
                    c[i][j] += A[i][k] * B[k][j]; 
                }
            }
        }
        return c; 
    }

    public static void main(String[] args) {
        int[][] A, B, C; 

        A = new int[][] { 
            {2, 3}, 
            {4, 6}  
        }; 

        B = new int[][] { 
            {11, 9}, 
            {2, 16}  
        }; 
        
       C = squareMatrixMultiply(A, B); 
       for(int[] c: C) { 
           System.out.println(Arrays.toString(c)); 
       }
    }
}
