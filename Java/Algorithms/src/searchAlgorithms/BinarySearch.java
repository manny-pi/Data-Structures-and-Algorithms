package searchAlgorithms;


public class BinarySearch {
    public static int binarySearch(Double[] data, Double value) { 
        int low = 0;
        int high = data.length - 1; 
        int mid = (int) (low + high) / 2; 
        
        while (low <= high) { 
            if (data[mid].equals(value)) {
                return mid;
            } else { 
                if (data[mid].compareTo(value) > 0) { 
                    high = mid - 1; 
                    mid = (int) (low + high) / 2; 
                } else if(data[mid].compareTo(value) < 0) { 
                    low = mid + 1; 
                    mid = (int) (low + high) / 2; 
                }
                return 0; 
            }
        }
        return -1; 
    }
    
    public static void main(String[] args) { 

    }
}
