package lists;

import java.util.Iterator;


public class Queue<E> implements Iterable<E> { 


	private class Node<T> { 
		T data; 
		Node<T> next; 

		private Node(T data) { 
			this.data = data;
			this.next = null; 
		}

		@Override 
		public String toString() { 

			return data.toString(); 
		}
		
		@Override
		public boolean equals(Object b) { 
			if (this == b) { 
				return true; 
			} 
			
			Node<T> B = null; 
			if (b instanceof Node) { 
				B = (Node<T>) b; 
				
			} else { 
				return false; 
			}
			
			if (this.data.equals(B.data)) { 
				return true; 
			}
			
			return false; 
		}
	}

	private Node<E> head; 
	private Node<E> tail; 
	private int size; 

	public Queue() { 
		this.head = null; 
		this.tail = null; 
	}

	/* Adds data to the end of the line */ 
	public void add(E data) { 
		this.addToEnd(data);
	}
	
	public E next() throws Exception {
		if (this.head == null) { 
			throw new Exception("Queue is Empty"); 
		} 
		
		E retval = this.head.data; 
		this.head = this.head.next; 
		this.size--; 
		
		return retval; 
	}
	
	public int size() { 

		return this.size; 
	}

	public Iterator<E> iterator() {
		return new Iterator<E>() {
			Node<E> curr = Queue.this.head; 
			E data; 

			@Override
			public boolean hasNext() {
				return curr != null;
			}

			@Override
			public E next() {
				data = curr.data; 
				curr = curr.next; 

				return data;
			} 
		};
	}

	@Override
	public String toString() { 
		Iterator<E> iter = this.iterator(); 
		String retval = "("; 
		while(iter.hasNext()) { 
			retval += iter.next(); 
			if (iter.hasNext()) retval += ", "; 
		}
		retval += ")"; 
		return retval; 
	}

	
	/* -- private methods -- */ 
	private void addToEnd(E data) { 
		if (this.head == null) { 
			this.head = new Node<>(data); 
			
		} else if (this.tail == null) { 
			this.tail = new Node<>(data); 
			this.head.next = this.tail; 
			
		} else { 
			Node<E> newTail = new Node<>(data); 
			this.tail.next = newTail;
			this.tail = newTail; 
		}
		this.size++; 
	}
	
	
	/* Test Queue */ 
	public static void main(String[] args) { 
		Queue<Integer> l = new Queue<>(); 
		for(int i = 0; i < 10; i++) { 
			Integer k = i; 
			l.add(k); 
		}
		
		System.out.println("l = " + l);
		System.out.println("Size = " + l.size()); 
		
		for(int i = 0; i < 5; i++) { 
			try { 
				System.out.println(l.next()); 
			} catch(Exception e) { 
				
			}
		}
		System.out.println("l = " + l);
		System.out.println("New size = " + l.size()); 
		
		l.add(12);
		l.add(24);
		for(Integer i: l) { 
			System.out.println(i); 
		}
		
		try { 
			System.out.println(l.next()); 
		} catch(Exception e) { 
			System.out.println(e.getMessage());
		}
	}
}