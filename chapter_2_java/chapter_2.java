package chapter_2_java;

public class chapter_2 {

	public chapter_2(){
		System.out.println("Running tests for chapter 2.");
		UnsortedSinglyLinkedList<Integer> l;
		UnsortedSinglyLinkedList<Character> m;

		//basic test cases
		l = new UnsortedSinglyLinkedList<Integer>();
		assert (l.isEmpty() == true) : "Error in basic test cases";

		l = new UnsortedSinglyLinkedList<Integer>(new Integer[]{1, 2, 3, 4, 5});
		assert (l.isEmpty() == false) : "Error in basic test cases";
		assert (l.toString().equals("head -> 1 -> 2 -> 3 -> 4 -> 5 -> end")) : "Error in basic test cases";
		assert (l.contains(1) == true) : "Error in basic test cases";
		assert (l.contains(2) == true) : "Error in basic test cases";
		assert (l.contains(3) == true) : "Error in basic test cases";
		assert (l.contains(4) == true) : "Error in basic test cases";
		assert (l.contains(5) == true) : "Error in basic test cases";
		assert (l.contains(6) == false) : "Error in basic test cases";

		m = new UnsortedSinglyLinkedList<Character>(new Character[]{'A', 'a', 'B', 'b', 'Z', 'z'});
		assert (m.toString().equals("head -> A -> a -> B -> b -> Z -> z -> end")) : "Error in basic test cases";
		assert (m.remove('A') == true) : "Error in basic test cases";
		assert (m.toString().equals("head -> a -> B -> b -> Z -> z -> end")) : "Error in basic test cases";
		assert (m.remove('z') == true) : "Error in basic test cases";
		assert (m.toString().equals("head -> a -> B -> b -> Z -> end")) : "Error in basic test cases";
		assert (m.remove('B') == true) : "Error in basic test cases";
		assert (m.toString().equals("head -> a -> b -> Z -> end")) : "Error in basic test cases";

		m = new UnsortedSinglyLinkedList<Character>();
		assert (m.insertAtTail('A') == true) : "Error in basic test cases";
		assert (m.insertAtHead('B') == true) : "Error in basic test cases";
		assert (m.insertAtTail('C') == true) : "Error in basic test cases";
		assert (m.insertAtHead('D') == true) : "Error in basic test cases";
		assert (m.insertAtTail('E') == true) : "Error in basic test cases";
		assert (m.insertAtHead('F') == true) : "Error in basic test cases";
		assert (m.toString().equals("head -> F -> D -> B -> A -> C -> E -> end")) : "Error in basic test cases";
		assert (m.contains('E') == true) : "Error in basic test cases";
		assert (m.contains(null) == false) : "Error in basic test cases";
		assert (m.contains('2') == false) : "Error in basic test cases";
		assert (m.contains('Z') == false) : "Error in basic test cases";
		assert (m.remove('A') == true) : "Error in basic test cases";
		assert (m.toString().equals("head -> F -> D -> B -> C -> E -> end")) : "Error in basic test cases";
		assert (m.remove('F') == true) : "Error in basic test cases";
		assert (m.toString().equals("head -> D -> B -> C -> E -> end")) : "Error in basic test cases";
		assert (m.remove('E') == true) : "Error in basic test cases";
		assert (m.toString().equals("head -> D -> B -> C -> end")) : "Error in basic test cases";
		assert (m.remove('B') == true) : "Error in basic test cases";
		assert (m.toString().equals("head -> D -> C -> end")) : "Error in basic test cases";
		assert (m.remove('E') == false) : "Error in basic test cases";
		assert (m.remove('A') == false) : "Error in basic test cases";
		assert (m.remove('D') == true) : "Error in basic test cases";
		assert (m.toString().equals("head -> C -> end")) : "Error in basic test cases";

		System.out.println("Basic tests passed.");

		//problem 2.1 test cases
		m = new UnsortedSinglyLinkedList<Character>(new Character[]{'A', 'A', 'b', 'c', 'd', 'c', 'A', 'd', 'E'});
		m.removeDuplicates();
		assert (m.toString().equals("head -> A -> b -> c -> d -> E -> end")) : "Error in Problem 1 test cases";
		m = new UnsortedSinglyLinkedList<Character>(new Character[]{'A', 'A', 'b', 'c', 'd', 'c', 'A', 'd', 'A'});
		m.removeDuplicates();
		assert (m.toString().equals("head -> A -> b -> c -> d -> end")) : "Error in Problem 1 test cases";

		m = new UnsortedSinglyLinkedList<Character>(new Character[]{'A', 'A', 'b', 'c', 'd', 'c', 'A', 'd', 'E'});
		m.removeDuplicatesWithoutSet();
		assert (m.toString().equals("head -> A -> b -> c -> d -> E -> end")) : "Error in Problem 1 test cases";
		m = new UnsortedSinglyLinkedList<Character>(new Character[]{'A', 'A', 'b', 'c', 'd', 'c', 'A', 'd', 'A', 'A'});
		m.removeDuplicatesWithoutSet();
		assert (m.toString().equals("head -> A -> b -> c -> d -> end")) : "Error in Problem 1 test cases";

		System.out.println("Problem 2.1 test cases passed.");

		l = new UnsortedSinglyLinkedList<Integer>(new Integer[]{4, 7, 19, 3, 20, 4, 1});
		assert (l.kthToLast(1) == 1) : "Error in Problem 2 test cases";
		assert (l.kthToLast(2) == 4) : "Error in Problem 2 test cases";
		assert (l.kthToLast(3) == 20) : "Error in Problem 2 test cases";

		System.out.println("Problem 2.2 test cases passed.");

		l = new UnsortedSinglyLinkedList<Integer>(new Integer[]{4, 7, 19, 3, 20, 4, 1});
		l.deleteNode(19);
		assert (l.toString().equals("head -> 4 -> 7 -> 3 -> 20 -> 4 -> 1 -> end")) : "Error in Problem 3 test cases";
		l.deleteNode(20);
		assert (l.toString().equals("head -> 4 -> 7 -> 3 -> 4 -> 1 -> end")) : "Error in Problem 3 test cases";
		l.deleteNode(7);
		assert (l.toString().equals("head -> 4 -> 3 -> 4 -> 1 -> end")) : "Error in Problem 3 test cases";

		System.out.println("Problem 2.3 test cases passed.");

		l = new UnsortedSinglyLinkedList<Integer>(new Integer[]{4, 7, 9, 12, 5, 1, 0, 19, 3, 20, 4, 1, 10, 53, 9, 10});
		l = l.partition(8);
		assert (l.isPartitioned(8) == true): "Error in Problem 4 test cases";
		l = l.partition(4);
		assert (l.isPartitioned(4) == true): "Error in Problem 4 test cases";
		l = l.partition(15);
		assert (l.isPartitioned(15) == true): "Error in Problem 4 test cases";
		l = l.partition(0);
		assert (l.isPartitioned(0) == true): "Error in Problem 4 test cases";
		l = l.partition(100);
		assert (l.isPartitioned(100) == true): "Error in Problem 4 test cases";

		System.out.println("Problem 2.4 test cases passed.");

		System.out.println("TODO: 2.5, 2.6, 2.7");
		//TODO: 2.5, 2.6, 2.7

	}

	public static void main(String[] args) {
		new chapter_2();
	}
}