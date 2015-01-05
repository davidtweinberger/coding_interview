package chapter_1_java;

public class chapter_1 {

	private StringManipulator _sm;

	public chapter_1(){
		System.out.println("Running tests for chapter 1.");
		_sm = new StringManipulator();

		//Problem 1.1
		assert (_sm.uniqueChars("David") == true) : "Error in Problem 1";
		assert (_sm.uniqueChars("DAVID") == false) : "Error in Problem 1";
		assert (_sm.uniqueChars("   DD       avid .../////") == false) : "Error in Problem 1";
		assert (_sm.uniqueChars("1234567890qwertyuiop-=[]asdfghjkl;'zxcvbnm,./?><:|}{+_ ") == true) : "Error in Problem 1";

		//Problem 1.2
		assert (_sm.reverse("DAVID").equals("DIVAD")) : "Error in Problem 2";
		assert (_sm.reverse("A man, a plan, a canal, panama").equals("amanap ,lanac a ,nalp a ,nam A")) : "Error in Problem 2";
		assert (_sm.reverse("This is a simple test.").equals(".tset elpmis a si sihT")) : "Error in Problem 2";

		//Problem 1.3
		assert (_sm.angrams("David", "aidDv") == true) : "Error in Problem 3";
		assert (_sm.angrams("David", "aiDv") == false) : "Error in Problem 3";
		assert (_sm.angrams("David is writing this code", "    acDddeghiiiiinorssttvw") == true) : "Error in Problem 3";
		assert (_sm.angrams("", "") == true) : "Error in Problem 3";

		//Problem 1.4
		assert (_sm.replaceSpaces("This is a small test.        ", 21).equals("This%20is%20a%20small%20test.")) : "Error in Problem 4";
		assert (_sm.replaceSpaces("Mr John Smith    ", 13).equals("Mr%20John%20Smith")) : "Error in Problem 4";

		//Problem 1.5
		assert (_sm.compress("aaabbbbcccccdef").equals("a3b4c5d1e1f1")) : "Error in Problem 5";
		assert (_sm.compress("asdfaaabbbcccdddeeefffggghhhiiijjjzxcv").equals("a1s1d1f1a3b3c3d3e3f3g3h3i3j3z1x1c1v1")) : "Error in Problem 5";
		assert (_sm.compress("asdfghjkl").equals("asdfghjkl")) : "Error in Problem 5";
		System.out.println("All tests passed.");

		//TODO
		//Problem 1.6
		//Problem 1.7
		//Problem 1.8
	}

	public static void main(String[] args) {
		new chapter_1();
	}

}