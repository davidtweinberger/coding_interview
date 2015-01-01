#!/usr/bin/python

"""
Answers to the questions in chapter 11 of Cracking the Coding Interview, in Python

David Weinberger (12/31/2014)
Brown University '16
davidtweinberger@gmail.com 
"""

def mergeAndSort(A, B):
	"""
	Given two sorted arrays A and B, A has enough room at the end to bold B.
	Merge B into A in sorted order.
	This algorithm merges the two arrays together by adding items to the end of A.
	"""
	curr = len(A) - 1 #current index
	Aindex = len(A) - len(B) - 1 #current position in A
	Bindex = len(B) - 1 #current position in B

	while(Bindex >= 0 and Aindex >= 0):
		if (A[Aindex] >= B[Bindex]):
			A[curr] = A[Aindex]
			Aindex -= 1
		else:
			A[curr] = B[Bindex]
			Bindex -= 1
		curr -= 1
	while (Bindex >= 0):
		A[curr] = B[Bindex]
		Bindex -= 1
		curr -= 1
	return A

def angramSort(angrams):
	"""
	Given a list of strings, sort it so that angrams are next to each other.
	"""

	table = {}
	for word in angrams:
		sortedword = reduce(lambda a, b: a + b, sorted(word))
		if not sortedword in table:
			table[sortedword] = set()
		table[sortedword].add(word)
	res = []
	for key in table:
		res += list(table[key])
	return res

def findInRotatedArray(A, ele, lo, hi):
	"""
	Given an array sorted in increasing order that has been rotated an unknown number
	of times, find the index of an element in it. 
	"""
	if (lo >= hi):
		return lo if A[lo] == ele else -1

	mid = lo + (hi - lo)/2

	if ele == A[mid]:
		return mid
	if ele < A[mid]:
		if ele == A[lo]:
			return lo
		if ele < A[lo]:
			return findInRotatedArray(A, ele, mid + 1, hi)
		if ele > A[lo]:
			return findInRotatedArray(A, ele, lo, mid - 1)
	if ele > A[mid]:
		if ele == A[hi]:
			return hi
		if ele < A[hi]:
			return findInRotatedArray(A, ele, mid + 1, hi)
		if ele > A[hi]:
			return findInRotatedArray(A, ele, lo, mid - 1)

def main():
	#tests go here

	#Problem 11.1
	print mergeAndSort([2, 2, 3, 4, 6, 9, None, None, None, None, None, None, None, None], [1, 3, 4, 5, 7, 8, 9, 10])

	#Problem 11.2
	print angramSort(["cat", "dog", "cta", "tac", "gdo", "tca", "dog", "dgo", "becca", "david", "ogd", "brown", "yale"])

	#Problem 11.3
	print findInRotatedArray([6, 8, 9, 10, 1, 3, 5], 9, 0, 6)

	#Problem 11.4

if __name__ == '__main__':
	main()