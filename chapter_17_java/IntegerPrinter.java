package chapter_17_java;
import java.io.*;

/*
 * Prints integers entered from the command line as words.
 * TODO - sort of janky, can probably be cleaned up a bit more.
 */

public class IntegerPrinter {

	//arrays storing string representation of numbers
	private String[] _numbers = new String[]{
		"zero", "one", "two", "three", "four", "five", 
		"six", "seven", "eight", "nine", "ten", "eleven", 
		"twelve", "thirteen", "fourteen", "fifteen", 
		"sixteen", "seventeen", "eighteen", "nineteen"};
	private String[] _tens = new String[]{"zero", "ten", 
		"twenty", "thirty", "forty", "fifty", "sixty", 
		"seventy", "eighty", "ninety"};
	private String[] _denominations = new String[]{
		"", "thousand ", "million ", "billion ", "trillion"};

	public IntegerPrinter(){
		//open up standard input
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		while(true){
			System.out.print("Enter an integer: ");
			try {
				try {
					int i = Integer.parseInt(br.readLine());
					printInteger(i);
				} catch(NumberFormatException ex){ // handle your exception
					System.err.println("Invalid number.");
				}
			} catch (IOException ioe) {
				System.err.println("IO error trying to read the integer.");
				ioe.printStackTrace();
				System.exit(1);
			}
		}
	}

	public void printInteger(int i){
		//deal with zero right away
		if (i == 0){
			System.out.println("zero");
			return;
		}
		java.lang.StringBuilder sb = new java.lang.StringBuilder();

		//negative will be added at the end, for now, make the number positive
		Boolean neg = false;
		if (i < 0){
			neg = true;
			i = -i;
		}

		//string representation of the integer
		String num = Integer.toString(i);

		//converts 3 places at a time (right to left), and then deals with left over digits
		int place = 3;
		while (place <= num.length()){
			//if the sequence of three digits is not zero, first insert the denomination
			if (!(num.substring(num.length() - place, num.length() - place + 3).equals("000"))){
				sb.insert(0, _denominations[place/3 - 1]);
			}

			//insert the result of the call to getstr (passing in the appropriate substring)
			sb.insert(0, getstr(num.substring(num.length() - place, num.length() - place + 3)));

			//increment place to move to the left
			place += 3;
		}

		if (place - num.length() == 1){
			//two digits left over
			sb.insert(0, _denominations[(num.length()-2)/3]);
			sb.insert(0, getstr("0" + num.substring(0, 2)));
		} else if (place - num.length() == 2){
			//one digit left over
			sb.insert(0, _denominations[(num.length()-1)/3]);
			sb.insert(0, getstr("00" + num.substring(0, 1)));
		}

		//otherwise no digits were left over (number of digits was divisible by three)

		//add "negative" at the beginning if necessary
		if (neg){
			sb.insert(0, "negative ");
		}

		//prints the number
		System.out.println(sb.toString());
	}

	public String getstr(String s){ 
		//returns a string corresponding to a three digit number passed in as a string
		java.lang.StringBuilder sb = new java.lang.StringBuilder();
		
		//there is a number in the hundreds place
		if (s.charAt(0) != '0'){
			sb.append(_numbers[Integer.parseInt(s.substring(0, 1))]);
			sb.append(" ");
			sb.append("hundred");
			sb.append(" ");
		}

		//there is a number in the tens place
		if (s.charAt(1) != '0'){
			//if it is not 1
			if (s.charAt(1) == '1'){
				sb.append(_numbers[Integer.parseInt(s.substring(1))]);
				sb.append(" ");
			//teens are a special case
			} else {
				sb.append(_tens[Integer.parseInt(s.substring(1, 2))]);
				sb.append(" ");
				if (s.charAt(2) != '0') {
					sb.append(_numbers[Integer.parseInt(s.substring(2, 3))]);
					sb.append(" ");
				}
		}

		//if there is no number in the tens place, but a number in the ones place
		} else if (s.charAt(2) != '0') {
			sb.append(_numbers[Integer.parseInt(s.substring(2))]);
			sb.append(" ");
		}

		//returns the string created
		return sb.toString();
	}

	public static void main(String[] args) {
		new IntegerPrinter();
	}
}