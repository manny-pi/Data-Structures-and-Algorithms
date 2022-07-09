package searchAlgorithms;


public class BinarySearch<T extends Comparable<? super T>> {
	public int binarySearch(T[] data, T value) { 
		int low = 0;
		int high = data.length - 1; 
		int mid = (int) (low + high) / 2; 

		while (low <= high) { 
			// Execute if MID = value 
			if (data[mid].equals(value)) {
				return mid;

			// Execute if MID > value 
			} else if (data[mid].compareTo(value) > 0) { 
				high = mid - 1; 
				mid = (int) (low + high) / 2; 

			// Execute if MID < value 
			} else if(data[mid].compareTo(value) < 0) { 
				low = mid + 1; 
				mid = (int) (low + high) / 2; 

			}
		}

		return -1; 
	}


	/* Test algorithm */ 
	public static void main(String[] args) { 
		BinarySearch<Integer> bs = new BinarySearch<>(); 
		Integer[] nums = new Integer[] {1, 2, 3, 4}; 

		System.out.println(bs.binarySearch(nums, 3));
	}
}
