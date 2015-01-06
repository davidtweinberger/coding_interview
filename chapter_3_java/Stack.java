package chapter_3_java;

public class Stack<T extends java.lang.Comparable<T>> {

	private Node<T> _top;

	public Stack(){
		_top = null;
	}

	public Stack(T[] elements){
		_top = null;
		for (int i=0; i<elements.length; i++){
			push(elements[i]);
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

	public void push(T data){
		_top = new Node<T>(data, _top);
	}

	public T pop(){
		if (_top == null){
			return null;
		}
		Node<T> temp = _top;
		_top = _top.getNext();
		return temp.getData();
	}

	public T peek(){
		if (_top == null){
			return null;
		}
		return _top.getData();
	}

	public Boolean isEmpty(){
		return (_top == null);
	}
}