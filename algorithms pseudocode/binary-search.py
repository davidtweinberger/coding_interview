#! /usr/bin/python

def binary_search(A, lo, hi, x):
	if lo >= hi:
		return A[lo] == x
	
	mid = (lo + hi) / 2

	if A[mid] == x:
		return True
	if A[mid] < x:
		return binary_search(A, mid+1, hi, x)
	if A[mid] > x:
		return binary_search(A, lo, mid-1, x)


if __name__ == "__main__": 
	array = [1, 2, 3, 4, 6, 7, 8, 9, 10];
	toFind = 5;
	print str(binary_search(array, 0, len(array)-1, toFind))