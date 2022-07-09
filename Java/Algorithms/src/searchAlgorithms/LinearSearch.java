package searchAlgorithms;

import java.util.Random;
import java.util.Arrays; 

public class LinearSearch<T> {

    public int linearSearch(T[] data, Object value) { 
        for (int i = 0; i < data.length; i++) { 
            if (data[i].equals(value)) return i; 
        }

        return -1; 
    }
    
    /* Test algorithm */ 
    public static void main(String[] args) { 
    	LinearSearch<Double> ls = new LinearSearch<>(); 
        Random random = new Random(); 
        Double[] data = new Double[10]; 
        for (int i = 0; i < 10; i++) { 
            data[i] = random.nextDouble() * 100;
        }

        double val1 = data[5]; 
        double val2 = 34.4f; 
        
        System.out.println("Data: " + Arrays.toString(data)); 

        System.out.printf("val1: %f -> result: %d\n", val1, ls.linearSearch(data, val1)); 
        System.out.printf("val2: %f -> result: %d\n", val2, ls.linearSearch(data, val2)); 

    }
}
