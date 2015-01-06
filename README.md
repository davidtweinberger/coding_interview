coding_interview
================

Coding Interview Practice (in Python, Java and C)

David Weinberger, Brown University '16

*Updated January, 2014*

###Instructions!
The code is structured as a set of directories, each of which is named after the corresponding chapter and the language in which it is written (e.g., chapter_1_python).  Each directory contains an executable file with the name of the chapter (e.g., chapter_1.py).
- Python:
 - Add execute permissions to the file by typing into a shell:
 ```
 $ chmod +x <filename>.py
 ```
 - Execute the file by typing:
 ```
 $ python <filename>.py
 ```
 - Each executable python file ends with a mainline and a main() function, that executes the test cases:
 ```python
 def main():
 	#test cases here
 
 if __name__ == "__main__":
 	main()
 ```
- Java:
 - Compile the code by typing into a shell (in the correct directory):
 ```
 $ javac *.java
 ```
 - From the parent directory, run the code using the following command:
 ```
 $ java <folder/package name>.<filename>
 # for example, java chapter_1_java.chapter_1 
 ```
 - I used assert statements within the code.  To enable these, run the file using the -ea flag:
 ```
 $ java -ea <folder/package name>.<filename>
 # for example, java -ea chapter_1_java.chapter_1
 ```


That's all there is!
