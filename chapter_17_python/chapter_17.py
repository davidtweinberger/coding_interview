#!/usr/bin/python

"""
Answers to the questions in chapter 17 of Cracking the Coding Interview, in Python

David Weinberger (12/31/2014)
Brown University '16
davidtweinberger@gmail.com 
"""

def swapInPlace(tup):
	"""
	Swaps a and b without using temp variables
	"""
	a, b = tup

	a += b
	b = a - b
	a -= b

	return (a, b)

def ticTacToeEvaluator(arr):
	"""
	Determines whether "X" or "O" has won a game of Tic-tac-toe, or neither.
	A list of rows is passed in as the argument.
	"""
	for row in arr:
		if len(set(row)) == 1 and row[0]:
			print row[0] + " won! (row)"
	for col in zip(*arr):
		if len(set(col)) == 1 and col[0]:
			print col[0] + " won! (col)"
	if len(set([arr[0][0], arr[1][1], arr[2][2]])) == 1 and arr[0][0]:
		print arr[0][0] + " won! (diagonal)"
	if len(set([arr[2][0], arr[1][1], arr[0][2]])) == 1 and arr[2][0]:
		print arr[2][0] + " won! (diagonal)"	
	for row in arr:
		print row

def factorialZeroes(n):
	"""
	Returns the number of trailing zeroes at the end of n!
	"""
	count = 0
	for i in range(n+1):
		num = i
		while num != 0 and num % 5 == 0:
			count += 1
			num = num / 5
	return count

def main():
	#tests go here

	#Problem 17.1
	print swapInPlace((10, 5))

	#Problem 17.2
	ticTacToeEvaluator([["X", "O", "X"], ["O", "O", "O"], ["O", "X", "X"]])

	#Problem 17.3
	print factorialZeroes(75)

if __name__ == '__main__':
	main()