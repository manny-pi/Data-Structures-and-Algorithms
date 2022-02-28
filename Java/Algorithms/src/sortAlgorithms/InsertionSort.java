package sortAlgorithms;

import java.util.Arrays; 


public class InsertionSort {

    public static void insertionSort(int[] nums) { 
        int key; 
        int j; 

        for(int i = 1; i < nums.length - 1; i++) { 
            key = nums[i]; 
            j = i - 1; 

            while (j >= 0 && nums[j] > key) { 
                nums[j + 1] = nums[j]; 
                nums[j] = key; 
                j -= 1; 
            }
        }    
    }

    public static void main(String[] args) { 
         int[] nums = new int[] {11, 5, 3, 2, 5, 7, 8, 9, 42}; 
         System.out.println("Original: " + Arrays.toString(nums)); 
         
         insertionSort(nums);

         System.out.println("Sorted: " + Arrays.toString(nums));
    }
}
