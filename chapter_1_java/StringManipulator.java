package chapter_1_java;

public class StringManipulator {

	private String _string;

	public StringManipulator(String s){
		_string = s;
	}

	public void setString(String s){
		_string = s;
	}

	//Methods for chapter 1
	public Boolean uniqueChars(){
		//Set will contain letters - use the Character type for the generic (cannot use primitive char)
		java.util.HashSet<Character> set = new java.util.HashSet<Character>();
		//Iterates through the string
		for (int i=0; i<_string.length(); i++){
			if (set.add(_string.charAt(i)) == false){
				return false;
			}
		}
		//finished, all chars are unique
		return true;

	}

}