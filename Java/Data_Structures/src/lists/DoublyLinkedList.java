package lists;

import java.util.Iterator;


public class DoublyLinkedList<E> implements Iterable<E> { 

	private class Node<T> { 
        Node<T> prev; 
        Node<T> next; 
		T data; 

		private Node(T data) { 
			this.data = data;

            this.prev = null;
			this.next = null; 
		}

		@Override 
		public String toString() { 

			return data.toString(); 
		}
	}

	private Node<E> head; 
	private int size; 

	public DoublyLinkedList() { 
		this.head = null; 
	}

	public void add(E data) { 
		if (this.head == null) { 
			this.head = new Node<E>(data);
            this.head.prev = null; 
            this.head.next = null; 
			
		} else { 
			Node<E> curr = head; 
			while (curr.next != null) { 
				curr = curr.next;
			}
            // Add the new Node
			curr.next = new Node<E>(data); 

            // Set the previous Node of the new Node
            Node<E> newNode = curr.next; 
            newNode.prev = curr; 
		}
		this.size++; 
	}
	
	public boolean remove(E data) {
        if (this.head == null) { 

        }
        
		if (head.data.equals(data)) { 
            Node<E> oldHead = this.head; 
            Node<E> newHead = this.head.next; 

            // Execute if the head is the only element in the list
            if(oldHead.next == null) { 
                this.head = null; 
            } else { 
                this.head = newHead; 

            }

            
			this.head = this.head.next; 
            this.head.prev = null; 
			
		} else { 
			Node<E> curr = this.head; 
			while(curr.next != null) { 

                E currData = curr.next.data; 
				if (currData.equals(data)) { 
					Node<E> prev = curr.prev;
                    Node<E> next = curr.next; 

                    prev.next = next; 
                    next.prev = prev; 
                    
					return true;
				}
			}
		}
		return false; 
	}	
	
	public E get(int index) { 
		E retval = null; 
		if (index > this.size - 1 || index < 0) { 
			throw new IllegalArgumentException("Index out of range"); 
		}
		int i = 0; 
		for(E e: this) { 
			if (i == index) {
				retval = e; 
				break; 
			}
			i++; 
		}
		
		return retval; 
	}

	public int size() { 

		return this.size; 
	}

	public Iterator<E> iterator() {
		return new Iterator<E>() {
			Node<E> curr = DoublyLinkedList.this.head; 
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

	public static void main(String[] args) { 
		DoublyLinkedList<Integer> l = new DoublyLinkedList<>(); 
		for(int i = 0; i < 10; i++) { 
			Integer k = i; 
			l.add(k); 
		}
		System.out.println(l);
        l.remove(1);
	}
}