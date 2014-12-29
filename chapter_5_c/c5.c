//Chapter 5: Bit Manipulation
//David Weinberger

/*
Answers to the questions in chapter 5 of Cracking the Coding Interview, in C

David Weinberger (12/22/2014)
Brown University '16
davidtweinberger@gmail.com
*/

#include <stdlib.h>
#include <stdio.h>
#define UNUSED(x) (void)(x)

//Declarations
void insertInto(int *N, int *M, int i, int j);

int main(int argc, char **argv) {

	//cmd line input is not parsed
	UNUSED(argc);
	UNUSED(argv);

	//Problem 5.1
	int N = 1024; 	//binary = 10000000000
	int M = 19; 	//binary = 10011
	int i = 2;
	int j = 6;
	insertInto(&N, &M, i, j);
	printf("N is %d in decimal notation\n", N);

	//Problem 5.2

	//Problem 5.3

	//Problem 5.4

	//Problem 5.5

	//Problem 5.6

	//Problem 5.7

	//Problem 5.8

	return 0;
}

void insertInto(int *N, int *M, int i, int j){
	/*	Args:
			N, M: two 32-bit integers
			i, j: two valid bit positions
		
		This function inserts M into N such that M starts at bit j and ends at bit i.
		Assume that there is enough space to fit all of M.

		Example:

			N = 10000000000, M = 10011, i = 2, j = 6

		Output:

			N = 10001001100 (N itself is changed as a pointer to N is passed in.)
	*/

	int mask = (~0 << (j + 1)) | ((1 << i) - 1); //All 1's except where M will go
	*N = (*N & mask) | (*M << i); //AND N with the mask to clear the bits where M will go, and then OR with M shifted by the correct amount
	
}

int printBinaryRepresentation(double d){
	UNUSED(d);
	return 0;
}

int nextSmallestAndLargest(int i){
	UNUSED(i);
	return 0;
}

int numberOfBitsToFlip(int A, int B){
	UNUSED(A);
	UNUSED(B);
	return 0;
}

int swapOddAndEven(int *i){
	UNUSED(i);
	return 0;
}

int findMissingNumber(int *array){
	UNUSED(array);
	return 0;
}

int drawHorizontalLine(char *screen, int width, int x1, int x2, int y){
	UNUSED(screen);
	UNUSED(width);
	UNUSED(x1);
	UNUSED(x2);
	UNUSED(y);
	return 0;
}