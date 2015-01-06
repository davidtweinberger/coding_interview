package chapter_3_java;

public class Queue<T extends java.lang.Comparable<T>> {

	private Node<T> _head;
	private Node<T> _tail;

	public Queue(){
		_head = null;
		_tail = null;
	}

	public Queue(T[] elements){
		_head = null;
		_tail = null;
		for (int i=0; i<elements.length; i++){
			enqueue(elements[i]);
		}
	}

	private class Node<T extends java.lang.Comparable<T>> {

		private T _data;
		private Node<T> _next;

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

		public void setData(T data){
			_data = data;
		}

		public T getData(){
			return _data;
		}

		public void setNext(Node<T> next){
			_next = next;
		}

		public Node<T> getNext(){
			return _next;
		}
	}

	public void enqueue(T data){
		if (_head == null) {
			_head = new Node<T>(data);
			_tail = _head;
		} else {
			_tail.setNext(new Node<T>(data));
			_tail = _tail.getNext();
		}
	}

	public T dequeue(){
		if (_head == null){
			return null;
		}
		Node<T> temp = _head;
		_head = _head.getNext();
		if (_head == null){
			_tail = null;
		}
		return temp.getData();
	}

	public Boolean isEmpty(){
		return (_head == null);
	}
}