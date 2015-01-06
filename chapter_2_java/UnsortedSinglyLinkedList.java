package chapter_2_java;

public class UnsortedSinglyLinkedList<T extends java.lang.Object> {

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
	private class Node<T>{

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

}