package sortAlgorithms;

import java.util.Arrays; 


public class SelectionSort {
    
    public static void selectionSort(int[] nums) { 
        int smallestIndex; 
        int temp;
        for(int i = 0; i < nums.length; i++){ 
            smallestIndex = i; 
            
            // Find the smallest element in nums[i.. j]
            for(int j = i + 1; j < nums.length; j++) { 
                if (nums[smallestIndex] > nums[j]) { 
                    smallestIndex = j; 
                }
            }

            // Swap A[i] and the smallest element 
            temp = nums[i]; 
            nums[i] = nums[smallestIndex]; 
            nums[smallestIndex] = temp; 
        }
    }

    public static void main(String[] args) { 
        int[] nums = new int[] {11, 5, 3, 2, 5, 7, 8, 9, 42}; 
        System.out.println("Original: " + Arrays.toString(nums)); 
        
        selectionSort(nums);

        System.out.println("Sorted: " + Arrays.toString(nums));
    }
}


