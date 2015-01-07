package chapter_17_java;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Scanner;
import java.util.Hashtable;
import java.nio.charset.StandardCharsets;

public class DocumentParser {
	
	private Hashtable<String, Integer> _table;
	
	public DocumentParser() {
		_table = new Hashtable<String, Integer>();
	}

	public void readFileToTable(String fileName) {
		//adds the words (removing punctuation) from the file to the hashtable, mapping from word to occurrences.
		Path path = Paths.get(fileName);
		try (Scanner scanner =  new Scanner(path, StandardCharsets.UTF_8.name())) {
			while (scanner.hasNextLine()){
				String nextline = scanner
									.nextLine()
									.toLowerCase()
									.replaceAll("(?!\")[\\p{Punct}&&[^']]", " ")
									.replaceAll("'", "");
				String[] words = nextline.split(" ");
				for (String word : words){
					if (_table.containsKey(word) == false){
						_table.put(word, 1);
					} else {
						_table.put(word, _table.get(word) + 1);
					}
				}
			}
		} catch (IOException ioe){
			ioe.printStackTrace();
			System.exit(1);
		}
		System.out.println(_table);
	}

	public String parseToSentence(String s, int start, int end){
		//parses a sequence of words with no spaces separating them into a sentence.
		//uses the letters in [start, end)
		
		return null;
	}
	
	public static void main(String[] args) {
		if (args.length == 0){
			System.err.println("Error - needs a source dictionary.");
			System.exit(1);
		}
		DocumentParser dp = new DocumentParser();
		for (int i=0; i<args.length; i++){
			dp.readFileToTable(args[i]);
		}
	}
}