package chapter_1_java;

public class chapter_1 {

	private StringManipulator _sm;

	public chapter_1(){
		System.out.println("Running tests for chapter 1.");

		//Problem 1.1
		_sm = new StringManipulator("David");
		assert (_sm.uniqueChars() == true) : "Error in Problem 1";
		_sm.setString("DAVID");
		assert (_sm.uniqueChars() == false) : "Error in Problem 1";
		_sm.setString("   DD       avid .../////");
		assert (_sm.uniqueChars() == false) : "Error in Problem 1";
		_sm.setString("1234567890qwertyuiop-=[]asdfghjkl;'zxcvbnm,./?><:|}{+_");
		assert (_sm.uniqueChars() == true) : "Error in Problem 1";

		//Problem 1.2

		System.out.println("All tests passed.");
	}

	public static void main(String[] args) {
		new chapter_1();
	}

}