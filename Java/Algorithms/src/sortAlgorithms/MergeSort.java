package sortAlgorithms;

import java.util.Arrays; 


public class MergeSort {
    public static void mergerSort(int[] nums) {
        if (nums.length <= 1) { 
            /* Do nothing */
            return; 

        } else { 
            mergeSort(nums, 0, nums.length - 1);
        }
    }
    
    public static void mergeSort(int[] nums, int leftBound, int rightBound) { 
        if (leftBound < rightBound) { 
            int mid = (int) Math.floor((leftBound + rightBound) / 2); 
            mergeSort(nums, leftBound, mid);
            mergeSort(nums, mid + 1, rightBound);
            mergeSortAux(nums, leftBound, mid, rightBound); 
        }
    }

    public static void mergeSortAux(int[] nums, int leftBound, int mid, int rightBound) { 
        int n1 = mid - leftBound + 1; 
        int n2 = rightBound - mid; 

        int[] L = new int[n1 + 1], R = new int[n2 + 1]; 

        for (int i = leftBound; i <= n1; i++) { 
            L[i] = nums[i]; 
        }
        L[n1] = (int) Double.POSITIVE_INFINITY; 

        for (int j = mid + 1; j <= rightBound; j++) { 
            R[j - (mid + 1)] = nums[j]; 
        }
        R[n2] = (int) Double.POSITIVE_INFINITY; 

        int i = 0, j = 0; 
        for (int k = leftBound; k <= rightBound; k++) { 
            if (k <= mid)
                if (L[k] == Double.POSITIVE_INFINITY) { 
                    nums[k] = R[j];  
                    j++; 

            } else if (R[j] == Double.POSITIVE_INFINITY) { 
                R[k] = L[i]; 
                i++;
                
            } else {
                if (L[i] <= R[j]) { 
                    nums[k] = L[i]; 
                    i++; 
                } else { 
                    nums[k] = R[j]; 
                    j++; 
                }
            }
        }
    }

    public static void main(String[] args) { 
        int[] nums = new int[] {11, 5, 3, 2, 5, 7, 8, 9}; 
        System.out.println("Original: " + Arrays.toString(nums)); 
        
        mergeSort(nums, 0, nums.length - 1);

        System.out.println("Sorted: " + Arrays.toString(nums));
    }
}
