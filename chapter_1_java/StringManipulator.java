package chapter_1_java;

public class StringManipulator {

	//Methods for chapter 1
	public Boolean uniqueChars(String string){
		//Set will contain letters - use the Character type for the generic (cannot use primitive char)
		java.util.HashSet<Character> set = new java.util.HashSet<Character>();
		//Iterates through the string
		for (int i=0; i<string.length(); i++){
			if (set.add(string.charAt(i)) == false){
				return false;
			}
		}
		//finished, all chars are unique
		return true;

	}

	public String reverse(String string){
		//Turns string into a char array
		char[] str = string.toCharArray();
		int len = str.length;

		//Iterates and switches
		for (int i=0; i<len/2; i++){
			char temp = str[len - i - 1];
			str[len - i - 1] = str[i];
			str[i] = temp;
		}

		//makes string
		string = new String(str);
		return string;
	}

	public Boolean angrams(String s1, String s2){
		//table mapping from char to number of occurrences
		java.util.Hashtable<Character, Integer> table = new java.util.Hashtable<Character, Integer>();

		//add s1 to the table
		char[] str1 = s1.toCharArray();
		int len1 = str1.length;
		for (int i=0; i<len1; i++){
			if (table.get(str1[i]) != null){
				table.put(str1[i], table.get(str1[i]) + 1);
			}
			else {
				table.put(str1[i], 1);
			}
		}

		//remove s2 from the table, checking for differences
		char[] str2 = s2.toCharArray();
		int len2 = str2.length;
		for (int j=0; j < len2; j++){
			if (table.containsKey(str2[j]) == false){
				return false;
			}
			table.put(str2[j], table.get(str2[j]) - 1);
			if (table.get(str2[j]) == 0){
				table.remove(str2[j]);
			}
		}

		//if table is now empty, strings were equal
		if (table.isEmpty()){
			return true;
		}
		else{
			return false;
		}
	}
	
	/*
		Replaces all spaces in string with "%20"
		Args: string, the length of the "true string"
	*/
	public String replaceSpaces(String string, int stringlength){
		char[] str = string.toCharArray();
		//error checking
		if (str.length == 0){
			return "";
		}

		//represents the end of the string
		int end = str.length - 1;
		
		//last character that is not a space
		int curr = stringlength-1;

		//iterates backwards, filling in the string with %20
		while (curr > 0){
			if (!(str[curr] == ' ')){
				str[end] = str[curr];
				end--;
				curr--;
			} else {
				curr--;
				str[end] = '0';
				str[end-1] = '2';
				str[end-2] = '%';
				end -= 3;
			}
		}

		return new String(str);

	}

	public String compress(String s){
		//used to concatenate the compressed string
		java.lang.StringBuilder sb = new java.lang.StringBuilder();
		char prev = s.charAt(0);
		char curr = s.charAt(0);
		int count = 0;
		for (int i=0; i<s.length(); i++){
			curr = s.charAt(i);
			if (curr != prev){
				sb.append(prev);
				sb.append(count);
				prev = curr;
				count = 1;
			} else {
				count += 1;
			}
		}
		sb.append(prev);
		sb.append(count);
		return sb.toString().length() < s.length() ? sb.toString() : s;
	}

}