package lists;

import lists.SinglyLinkedList;
import java.security.Key;

public class Hashtable {
	
	
	private int hash(Key k) { 
		
		int M = 2; 
		return (k.hashCode() & 0x7fffffff % M); 
	}
    
}
