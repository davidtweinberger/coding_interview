package chapter_2_java;

public class UnsortedSinglyLinkedList<T extends java.lang.Comparable<T>> {

	private Node<T> _head;

	//basic constructor for the linked list
	public UnsortedSinglyLinkedList(){
		_head = null;
	}

	//other constructors
	public UnsortedSinglyLinkedList(T[] elements){
		_head = null;
		for (int i=0; i<elements.length; i++){
			insertAtTail(elements[i]);
		}
	}

	//toString method to print the list
	@Override
	public String toString(){
		java.lang.StringBuilder sb = new java.lang.StringBuilder();
		sb.append("head -> ");
		Node<T> curr = _head;
		while (curr != null){
			sb.append(curr.toString());
			sb.append(" -> ");
			curr = curr.getNext();
		}
		sb.append("end");
		return sb.toString();
	}

	//inner class representing a node in the list
	private class Node<T extends java.lang.Comparable<T>>{

		//node ivars
		private T _data;
		private Node<T> _next;

		//4 constructors
		public Node(){
			_data = null;
			_next = null;
		}
		public Node(T data){
			_data = data;
			_next = null;
		}
		public Node(Node<T> next){
			_data = null;
			_next = next;
		}
		public Node(T data, Node<T> next){
			_data = data;
			_next = next;
		}

		//accessors and mutators
		public T getData(){
			return _data;
		}

		public void setData(T data){
			_data = data;
		}

		public Node<T> getNext(){
			return _next;
		}

		public void setNext(Node<T> next){
			_next = next;
		}

		@Override
		public String toString(){
			return _data.toString();
		}

		public int compareTo(T obj){
			if (this.getData().compareTo(obj) < 0){
				return -1;
			} else if (this.getData().compareTo(obj) == 0){
				return 0;
			} else {
				return 1;
			}
		}
	}

	//basic methods

	public Boolean isEmpty(){
		return (_head == null);
	}

	public Boolean insertAtTail(T data){
		if (data == null){
			return false;
		}
		if (_head == null){
			_head = new Node<T>(data);
		} else {
			Node<T> curr = _head;
			while (curr.getNext() != null){
				curr = curr.getNext();
			}
			curr.setNext(new Node<T>(data));
		}
		return true;
	}

	public Boolean insertAtHead(T data){
		if (data == null){
			return false;
		}
		_head = new Node<T>(data, _head);
		return true;
	}

	public Boolean remove(T data){
		if (data == null){
			return false;
		} else if (_head == null){
			return false;
		} else if (_head.getData().equals(data)){
			_head = _head.getNext();
			return true;
		} else {
			Node<T> curr = _head;
			while ((curr.getNext() != null) && (curr.getNext().getData().equals(data) == false)){
				curr = curr.getNext();
			}
			if (curr.getNext() == null){
				return false;
			}
			else {
				curr.setNext(curr.getNext().getNext());
				return true;
			}
		}
	}

	public Boolean contains(T data){
		if (data == null){
			return false;
		} else if (_head == null){
			return false;
		} else {
			Node<T> curr = _head;
			while (curr.getData().equals(data) == false){
				curr = curr.getNext();
				if (curr == null){
					return false;
				}
			}
			return true;
		}
	}

	/* LINKED LIST ALGORITHMS */

	//stable algorithm to remove duplicates from a linked list.
	public void removeDuplicates(){
		Node<T> curr = _head;
		if (curr == null){
			return;
		}

		//Uses a HashSet starting out with the data from the first node
		java.util.HashSet<T> set = new java.util.HashSet<T>();
		set.add(curr.getData());

		while (curr.getNext() != null){
			//adds the data from the next node at each iteration
			if (set.add(curr.getNext().getData()) == false){
				//if next node's data is in the set already, then delete the next node
				//and go to the next iteration without updating curr
				curr.setNext(curr.getNext().getNext());
				continue;
			}
			//otherwise, update curr and make sure it is not null
			curr = curr.getNext();
			if (curr == null){
				break;
			}
		}
	}

	//stable algorithm to remove duplicates from a linked list.
	public void removeDuplicatesWithoutSet(){
		Node<T> curr = _head;
		Node<T> temp = curr; 
		if (curr == null){
			return;
		}

		//outer while loop iterates through all nodes
		while (curr != null){
			//keep track of the current node
			temp = curr;
			//inner while loop iterates through nodes after curr and removes duplicates
			while (curr != null && curr.getNext() != null){
				if (curr.getNext().getData() == temp.getData()){
					curr.setNext(curr.getNext().getNext());
				} else {
					curr = curr.getNext();
				}
			}
			//curr updates back to temp's next
			curr = temp.getNext();
		}
	}

	public T kthToLast(int k){
		k--;
		Node<T> curr = _head;
		Node<T> kth = curr;
		if (curr == null || k < 0){
			return null;
		}

		for (int i=0; i<k; i++){
			curr = curr.getNext();
			if (curr == null){
				return null; //list is too short
			}
		}

		while (curr.getNext() != null){
			curr = curr.getNext();
			kth = kth.getNext();
		}

		return kth.getData();
	}

	public void deleteNode(T data){
		//deletes the node with data given access only to that node.
		//does not work on the head or the tail nodes
		Node<T> toDelete;
		if ((toDelete = getNode(data)) != null){
			toDelete.setData(toDelete.getNext().getData());
			toDelete.setNext(toDelete.getNext().getNext());
		}
	}

	private Node<T> getNode(T data){
		//searches for and returns the first instance of a node with the specified data
		if (data == null){
			return null;
		} else if (_head == null){
			return null;
		} else {
			Node<T> curr = _head;
			while (curr.getData().equals(data) == false){
				curr = curr.getNext();
				if (curr == null){
					return null;
				}
			}
			return curr;
		}
	}

	public UnsortedSinglyLinkedList<T> partition(T val){
		//returns a new LinkedList instance that is partitioned around a value
		if (val == null){
			return null;
		}
		UnsortedSinglyLinkedList<T> newlist = new UnsortedSinglyLinkedList<T>();
		Node<T> curr = _head;
		while (curr != null){
			if (curr.compareTo(val) < 0){
				newlist.insertAtHead(curr.getData());
			}
			else {
				newlist.insertAtTail(curr.getData());
			}
			curr = curr.getNext();
		}
		return newlist;
	}

	public Boolean isPartitioned(T val){
		//returns true if the list is partitioned around some value val
		//partitioned means that all values less than val come before all values greater than or equal to val.
		Node<T> curr = _head;
		if (curr == null){
			return true;
		}
		while (curr.compareTo(val) < 0){
			curr = curr.getNext();
			if (curr == null){
				return true;
			}
		}
		while (curr.compareTo(val) >= 0){			
			curr = curr.getNext();
			if (curr == null){
				return true;
			}
		}
		return false;
	}

}