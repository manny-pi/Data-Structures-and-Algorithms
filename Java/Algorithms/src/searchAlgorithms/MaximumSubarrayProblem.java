package searchAlgorithms;


public class MaximumSubarrayProblem {
    
    public static double[] findMaxCrossingSubarray(double[] A, int low, int mid, int high) { 
        double leftSum = Double.NEGATIVE_INFINITY; 
        double sum = 0; 
        int maxLeft = mid; 
        for (int i = mid; i >= low; i--) { 
            sum = sum + A[i]; 
            if (sum > leftSum) { 
                leftSum = sum; 
                maxLeft = i; 
            }
        }
        
        double rightSum = Double.NEGATIVE_INFINITY; 
        sum = 0; 
        int maxRight = mid + 1; 
        for (int j = mid + 1; j < high; j++) { 
            sum = sum + A[j]; 
            if (sum > rightSum) { 
                rightSum = sum; 
                maxRight = j; 
            }
        }
        return new double[]{maxLeft, maxRight, leftSum + rightSum}; 
    }
    
    public static double[] findMaximumSubarray(double[] A, int low, int high) { 
        if (high == low) { 
            return new double[] {low, high, A[low]}; 
        } 
        
        int mid = (int) Math.floor((low + high) / 2); 
        double[] left = findMaximumSubarray(A, low, mid); 
        double[] right = findMaximumSubarray(A, mid + 1, high); 
        double[] cross = findMaxCrossingSubarray(A, low, mid, high); 
        
        double leftSum = left[2], rightSum = right[2], crossSum = cross[2]; 
        if (leftSum >= rightSum && leftSum >= crossSum) { 
            return left; 
        }
        else if (rightSum >= leftSum && rightSum >= crossSum) { 
            return right; 
        }
        return cross; 
    }
    
    public static void main(String[] args) { 
        double[] prices = new double[] {13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, - 5, -22, 15,-4, 7};
        double[] sub = findMaximumSubarray(prices, 0, prices.length - 1); 
        
        int low = (int) sub[0], high = (int) sub[1]; 
        double maxValue = sub[2]; 
        
        System.out.println("Max Subarray: ");
        for(int i = low; i <= high; i++) { 
            System.out.print(prices[i] + " "); 
        }
        System.out.println("\nMax value: " + maxValue); 
    } 
}