package matrices;


import java.util.ArrayList;


public class SquareMatrixMultiplicationRecursive {
    
    public static int[][] squareMatrixMultiplication(int[][] A, int[][] B) { 
        ArrayList<ArrayList<Integer>> A1, B2; 

        int rows = A.length, cols = A[0].length; 
        for(int i = 0; i < rows; i++) {
            for(int j = 0; j < cols; j++) { 
                try { 

                    /* */ 

                } catch(IndexOutOfBoundsException e) { 
                    
                    /* */ 

                }
            }
        } 

        return null; 
    }
    
    /* Note: int i is just to stop the compiler from complaining; redundant parameter*/ 
    public static ArrayList<ArrayList<Integer>> squareMatrixMultiplication(int[][] A, int[][] B, int i) {
        int n = A.length; 
        
        if (n == 1) {
            
        } else {
            
            /* Calculate the start, mid, and end indexes */
            int start = 0, end = n - 1; 
            int mid = (int) Math.floor((start + end) / 2); 
            
            /* Partition A, B, and C into submatrices */ 
            int[][] A11 = subarray(A, start, mid, start, mid); 
            int[][] A12 = subarray(A, start, mid, mid + 1, end); 
            int[][] A21 = subarray(A, mid + 1, end, start, end);
            int[][] A22 = subarray(A, mid + 1, end, mid + 1, end);
            
            int[][] B11 = subarray(A, start, mid, start, mid); 
            int[][] B12 = subarray(A, start, mid, mid + 1, end); 
            int[][] B21 = subarray(A, mid + 1, end, start, end);
            int[][] B22 = subarray(A, mid + 1, end, mid + 1, end);
            
        }
        
        return null; 
    }
    
    public static int[][] subarray(int[][] nums, int rowStart, int rowEnd, int colStart, int colEnd) {
        int n = nums.length; 
        int[][] sub = new int[n][n]; 
        for(int i = rowStart; i <= rowEnd; i++) { 
            for(int j = colStart; j <= colEnd; j++) { 
                sub[i - rowStart][j - colStart] = nums[i][j]; 
            }
        }
        
        return sub; 
    }
    
    public static int[][] sum(int[][] A, int[][] B) { 
        int n = A.length; 
        int[][] sum = new int[n][n];
        
        for(int i = 0; i < n; i++) { 
            for(int j = 0; j < n; j++) {
                sum[i][j] = A[i][j] + B[i][j]; 
            }
        }
        
        return sum; 
    }
    
    public static void main(String[] args) { 
        
    }
}
