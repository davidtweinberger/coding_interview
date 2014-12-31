#!/usr/bin/python

"""
Answers to the questions in chapter 9 of Cracking the Coding Interview, in Python

David Weinberger (12/29/2014)
Brown University '16
davidtweinberger@gmail.com 
"""

def staircaseCounter(n_steps):
	"""
	A child is running up a staircase with n steps and can hop either 1 step, 
	2 steps, or 3 steps at a time.  This function counts the total number of
	ways the child can run up the stairs.  It's a simple recursive algorithm 
	with 3 recursive calls at each level and 4 base cases.  Runtime is bad - 
	O(3^n)
	"""

	#error handling
	if (n_steps == None or (type(n_steps) != int)):
		return 0

	#Base cases
	if (n_steps == 0):
		return 0
	if (n_steps == 1):
		return 1
	if (n_steps == 2):
		return 2
	if (n_steps == 3):
		return 4

	#can jump 1, 2, or 3 steps
	return staircaseCounter(n_steps - 1) + \
			staircaseCounter(n_steps - 2) + \
			 staircaseCounter(n_steps - 3)

def betterStaircaseCounter(n_steps):
	"""
	A child is running up a staircase with n steps and can hop either 1 step, 
	2 steps, or 3 steps at a time.  This function counts the total number of
	ways the child can run up the stairs.  Iterative Dynamic Programming 
	solution.  The runtime is linear O(n).  counts can be global to cache 
	solution between calls to this function to further improve runtime. (At 
	the worst case it will be linear, best case will be constant).
	"""

	#error handling
	if (n_steps == None or (type(n_steps) != int)):
		return 0

	#simple cases
	if (n_steps == 0):
		return 0
	if (n_steps == 1):
		return 1
	if (n_steps == 2):
		return 2
	if (n_steps == 3):
		return 4

	#array of zeroes of length n_steps, init the last three indices so it looks like [0, 0, ..., 0, 0, 4, 2, 1]
	counts = [0 for i in range(n_steps)]
	counts[-1] = 1
	counts[-2] = 2
	counts[-3] = 4

	#variable indexing into counts, beginning at the last index
	#i will be at least 0 because of the simple cases already handled
	i = n_steps - 4

	#loop through the array backwards
	while (i >= 0):
		counts[i] = counts[i+1] + counts[i+2] + counts[i+3]
		i -= 1

	#return what's in the first index of the array
	return counts[0]

def robotSolver(rows, cols, offLimits=set()):
	"""
	Imagine a robot sitting on the upper left corner of an X by Y grid.  The robot can
	only move in two directions: right and down.  How many possible paths are there for
	the robot to go from (0, 0) to (X, Y)?

	Args:
		rows - the number of rows
		cols - the number of cols
		offLimits is a set of points (row, column) that are "Off limits" - the robot cannot go there.

	Runtime and space complexity are O(rows * cols)
	"""

	#inits the grid as a list of rows (last row and column filled with ones)
	grid = [[0 for i in xrange(cols - 1)] + [1] for i in xrange(rows - 1)] + [[1 for i in xrange(cols)]]
	
	#fills in the grid with values, or 0 if off limits
	for r in xrange(rows-2, -1, -1):
		for c in xrange(cols-2, -1, -1):
			if not (r, c) in offLimits:
				grid[r][c] = grid[r][c+1] + grid[r+1][c]
			else:
				grid[r][c] = 0

	#returns what's in grid[0][0]
	return grid[0][0]

def findMagicIndex(array, lo, hi):
	"""
	A magic index in an array A[0...n-1] is defined to be an index such that A[i] == i.
	Given a sorted array of distinct integers, write a method to find a magic index, if 
	one exists, in array A.

	Args:
		array - a sorted list of integers (increasing order)
		lo - a valid lower bound in the array
		hi - a valid upper bound in the array
	"""

	#base case
	if (lo >= hi):
		return lo if (array[lo] == lo) else -1

	#find the mid index
	mid = int(lo + (hi - lo)/2)
	
	#if the element is less than the index, possible match is in the right half
	if array[mid] < mid:
		return findMagicIndex(array, mid + 1, hi)

	#if the element is greater than the index, possible match is in the left half
	elif array[mid] > mid:
		return findMagicIndex(array, lo, mid - 1)
	
	#found a match!
	else:
		return mid

def getAllSubsets(S, lo, hi):
	"""
	A function that returns all subsets of a set (modeled as a list)
	in the form of a list of lists.
	"""
	#removes duplicates
	S = list(set(S))

	#base case - subsets of a list of length 1 is an empty list and the list itself
	if (lo == hi):
		return [[], [S[lo]]]

	#subsets is all of the subsets of the list without the first element, 
	#and all of the subsets of the list with the first element
	subsets = getAllSubsets(S, lo+1, hi)
	subsets += map(lambda ele:[S[lo]] + ele, getAllSubsets(S, lo+1, hi))

	#returns the list of subsets
	return subsets

def getAllPermutations(string):
	"""
	Computes all permutations of a string of unique characters and returns them as a list of strings.
	Runtime is bad: O(len(string)!) but there's no way to improve it...
	"""

	#base cases
	if len(string) == 0:
		return [""]
	if len(string) == 1:
		return string
	if len(string) == 2:
		return [string] + [string[::-1]]

	#recursive calls
	subpermutations = getAllPermutations(string[1:]) #permutations of the string without the first character
	inserted = []
	for perm in subpermutations:
		for i in xrange(len(perm) + 1): #inserts the first character in the string into every possible position
			inserted.append(perm[:i] + string[0] + perm[i:])

	#returns inserted
	return inserted

def getParenthesesPermutations(n):
	"""
	A function that returns a list of all valid combinations of n pairs of parentheses
	(a list of strings).
	"""

	#base cases
	if (n==0):
		return [""]
	if (n==1):
		return ["()"]

	#recursive call
	newParenList = []
	parenList = getParenthesesPermutations(n-1)
	for perm in parenList:
		newParenList.append("()" + perm)
		newParenList.append(perm + "()")
		newParenList.append("(" + perm + ")")

	#returns newParenList without duplicates
	return list(set(newParenList))

def paintFill(screen, pixel, color):
	"""
	Uses a BFS algorithm to represent the "paint fill" function of an image editing program.
	Args:
		screen: a 2D list (a list of rows)
		pixel: (an (x, y) tuple of where to start)
		color: the new color to fill in (a string)
	"""

	#bounds checking function
	isInBounds = lambda x, y: False if (x >= len(screen[0]) or y >= len(screen) or x < 0 or y < 0) else True

	#error checking
	x, y = pixel
	if not isInBounds(x, y):
		return

	originalColor = screen[y][x]

	#BFS using list as a Queue
	Queue = []
	Visited = {} 
	Queue.append(pixel)
	while len(Queue):
		x, y = Queue.pop(0)
		screen[y][x] = color
		Visited[(x, y)] = True
		for i in range(x-1, x+2):
			for j in range(y-1, y+2):
				if isInBounds(i, j) and screen[j][i] == originalColor and (i, j) not in Visited:
					Queue.append((i, j))

	return screen

def centsRepresentations(n, denom): 
	#first call - denom is the largest coin denomination (in this case 25)
	"""
	Given an integer n, this function returns the number of ways that n cents 
	can be represented with quarters, dimes, nickels and pennies.

	NAIVE IMPLEMENTATION

	This problem can be thought about in the following way: assume that when 
	making change, you always give the coins in order from largest to smallest
	value.  Thus, for n cents, you can give a quarter, and then calculate the ways 
	of making change for n-25 cents with quarters or less; then assume you give a 
	dime first and calculate the number of ways of making change for n-10 cents 
	with dimes or less, and so on.
	"""
	#base cases:
	if (n<0):
		return 0
	if (n==0):
		return 1

	#recursive calls
	S = 0
	if (denom >= 25):
		S += centsRepresentations(n-25, 25)
	if (denom >= 10):
		S += centsRepresentations(n-10, 10)
	if (denom >= 5):
		S += centsRepresentations(n-5, 5)
	if (denom >= 1):
		S += centsRepresentations(n-1, 1)
	return S

def eightQueens():
	"""
	An algorithm that prints all ways of arranging 8 queens on an 8x8 board
	so that none share the same row, col or diagonal.

	TODO - naive
	"""
	from itertools import permutations #uses this module to generate all permutations of range(7)
	#each permutation represents the column index of the queen in each row - the first number in 
	#the permutation is the col index of the queen in row 1, etc. So all that needs to be checked 
	#is that queens don't overlap diagonally.

	notdiagonal = lambda perm: True if \
		len(set(map(lambda ele : ele[1] + ele[0], [ele for ele in enumerate(perm)]))) == 8 \
		and len(set(map(lambda ele : ele[1] - ele[0], [ele for ele in enumerate(perm)]))) == 8 \
		else False

	perms = permutations(range(8))
	for perm in perms:
		if notdiagonal(perm):
			print ("|\n".join('|_' * i + '|Q' + '|_' * (7-i) for i in perm) + "|\n===\n")

def main():
	#Tests go here

	#Problem 9.1
	print staircaseCounter(10)
	print betterStaircaseCounter(10)

	#Problem 9.2
	print robotSolver(5, 6, set([(0, 1), (2, 0)]))

	#Problem 9.3
	assert findMagicIndex([0, 3, 4, 7], 0, 3) == 0, "Error"
	assert findMagicIndex([1, 2, 3, 4, 9, 10], 0, 5) == -1, "Error"
	assert findMagicIndex([-10, -3, 1, 3, 6, 9], 0, 5) == 3, "Error"

	#Problem 9.4
	print getAllSubsets([1, 2, 3, 4], 0, 3)

	#Problem 9.5
	print getAllPermutations("ABCD")

	#Problem 9.6
	print getParenthesesPermutations(4)

	#Problem 9.7
	screen = [	["BLUE" for i in range(5)],
				["BLUE", "GREY", "GREY", "GREY", "GREY"],
				["BLUE" for i in range(5)],
				["GREY", "GREY", "GREY", "GREY", "BLUE"],
				["BLUE" for i in range(5)],
				["BLUE" for i in range(5)],
				["GREY", "GREY", "BLUE", "GREY", "BLUE"],
				["BLUE" for i in range(5)],
				["BLUE", "GREY", "BLUE", "GREY", "BLUE"]]

	print paintFill(screen, (4, 8), "PINK")

	#Problem 9.8
	print centsRepresentations(200, 25)

	#Problem 9.9
	eightQueens()

	#Problem 9.10 - TODO
	#Problem 9.11 - TODO

if __name__ == '__main__':
	main()