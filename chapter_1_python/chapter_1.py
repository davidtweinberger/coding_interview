#!/usr/bin/python
import string

"""
Answers to the questions in chapter 1 of Cracking the Coding Interview, in Python
David Weinberger (12/21/2014)
Brown University '16
davidtweinberger@gmail.com 
"""

#Problem 1.1
def unique_chars(s):
	""" an algorithm which determines whether or not a string has unique characters
	uses the fact that sets contain distinct elements """
	char_set = set(s)
	return (len(char_set) == len(s))

#Problem 1.2
def reverse_str(s):
	""" an algorithm to reverse a null-terminated string
	trivial in python """
	return reversed(s) if s else ""

#Problem 1.3
def str_permut(s1, s2, ign=None, ignore_case=False):
	"""
	an algorithm that determines if a string is a permutation of another string
	in other words, if the two strings are angrams
	arguments:
		s1 			the first string
		s2 			the second string
		ign 		a set of characters to be ignored (removed from the strings) (optional)
		ignore_case	should case should be ignored (optional)
	"""
	#tests for bad input
	if (not s1 or not s2):
		return False

	#ignores case if specified
	if (ignore_case):
		s1 = s1.lower()
		s2 = s2.lower()

	#set of chars that are to be ignored (punctutation)
	if (not ign):
		ignore_set = {".", ",", ";", " ", ":", "?", "!", "\\", "/"} #defaults to this set
	else:
		ignore_set = ign

	#filter out the ignored characters
	f_s1 = filter(lambda c:c not in ignore_set, s1)
	f_s2 = filter(lambda c:c not in ignore_set, s2)

	#tests that strings are not empty after filtering
	if (not f_s1 or not f_s2):
		return False

	#sort the strings
	s_s1 = sorted(f_s1)
	s_s2 = sorted(f_s2)

	#tests for equality
	return s_s1 == s_s2

#Problem 1.4
def replace_spaces(s):
	""" an algorithm to replace spaces in a string with '%20'
	trivial in python """
	if not s:
		return ''
	return s.replace(" ", "%20")

#Problem 1.5
def compress_str(s):
	"""
	an algorithm to perform basic string compression using counts of repeated characters
	note - this is not in place (that's not really feasible in python)
	example:	aabcccccaaa --> a2b1c5a3
	returns the original string if it is shorter
	"""
	new_str = ''
	count = 0
	prev = None

	if not s:
		return ""

	for char in s:
		if not prev:
			prev = char
		if char != prev:
			new_str += prev
			new_str += str(count)
			count = 0
		count += 1
		prev = char

	if prev:
		new_str += prev
		new_str += str(count)

	return new_str if (len(new_str) < len(s)) else s

#Problem 1.6
def rotate(m, direction="Right"):
	"""
	an algorithm to rotate a matrix by 90 degrees in place (not sure how it makes a 
	difference that each pixel is 4 bytes)
	pretty trivial in python using zip(), reversed() and list comprehension
	"""
	if not m:
		return []
	if direction=="Right":
		count=1
	elif direction=="Left":
		count=3
	for i in range(count):
		m = [list(reversed(elem)) for elem in zip(*m)] #looked up zip(*m) online ....
	return m

#Problem 1.7
def zero(m):
	"""
	an algorithm such that if an element in a MxN matrix is 0, its row and column are set to 0
	matrix m is given as a list of rows
	"""
	if not m:
		return []

	rows = len(m)
	cols = len(m[0])

	#a new array that will eventually be returned, inited with all 1's
	ret = [[1 for i in range(cols)] for j in range(rows)]

	#iterates through the matrix, looking for 0's
	#when a 0 is found in m, the corresponding row and column in ret are filled with 0's
	for row, i in enumerate(m):
		for col, j in enumerate(i):
			if (j == 0):
				ret[row] = [0 for i in range(cols)]
				for k in range(rows):
					ret[k][col] = 0

	#1's left in ret are replaced with the original values
	for row, l in enumerate(ret):
		for col, elem in enumerate(l):
			if elem:
				ret[row][col] = m[row][col]

	return ret

#Problem 1.8
def is_rotation(s1, s2):
	"""
	an algorithm that checks if a string s2 is a rotation of another string s1
	using is_substring method only once.
	trivial in python
	"""
	if not s1 or not s2:
		return False
	return True if string.find(s1+s1, s2) > 0 else False

#main function with tests
def main():

	#tests unique_chars function
	assert unique_chars('david') == False, "Error"
	assert unique_chars('David') == True, "Error"
	assert unique_chars('rebecca') == False, "Error"
	assert unique_chars('marie') == True, "Error"
	assert unique_chars('leonard') == True, "Error"

	#tests str_permut function
	assert str_permut('David', 'Ddavi') == True, "Error"
	assert str_permut('David', 'ddavi') == False, "Error"
	assert str_permut('David', 'Rebecca') == False, "Error"
	assert str_permut('', '') == False, "Error"
	assert str_permut(None, None) == False, "Error"
	assert str_permut('   ', ' ') == False, "Error"
	assert str_permut('.;', '  ') == False, "Error"
	assert str_permut('.;/', '.;/') == False, "Error"
	assert str_permut('David is at home for Hanukkah', 'home is at Hanukkah for David') == True, "Error"
	assert str_permut('David,,,. is at home!?? for Hanukkah;;', 'home///;? is. a!t Han!u!kk!ah f\or Da,vid') == True, "Error"
	assert str_permut('David', 'Daaaaaaaaaaaaavid', ign={'a'}) == True, "Error"
	assert str_permut('David is working', 'Becca is working', ign={'D', 'a', 'v', 'i', 'd', 'B', 'e', 'c'}) == True, "Error"
	assert str_permut('DAVID', 'david', ignore_case=True) == True, "Error"

	#tests replace_spaces function
	assert replace_spaces("hello world ") == "hello%20world%20", "Error"
	assert replace_spaces("   ") == "%20%20%20", "Error"
	assert replace_spaces(None) == '', "Error"
	assert replace_spaces('') == '', "Error"

	#tests compress_str function
	assert compress_str("aabcccccaaa") == "a2b1c5a3", "Error"
	assert compress_str("aabccccca") == "a2b1c5a1", "Error"
	assert compress_str("") == "", "Error"
	assert compress_str(None) == "", "Error"
	assert compress_str("daaaaavvvvvviiiidBecccaaaaaaW") == "d1a5v6i4d1B1e1c3a6W1", "Error"
	assert compress_str("david") == "david", "Error"
	assert compress_str("ddaavviidd") == "ddaavviidd", "Error"

	#tests rotate function
	assert rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[7, 4, 1],[8, 5, 2],[9, 6, 3]], "Error"
	assert rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]], direction="Left") == [[3, 6, 9], [2, 5, 8], [1, 4, 7]], "Error"
	assert rotate([]) == [], "Error"
	assert rotate(None) == [], "Error"

	#tests zero function
	assert zero([[1, 2, 3, 4, 5], [7, 4, 5, 0, 5], [2, 0, 4, 7, 3], [8, 2, 5, 7, 1], [5, 3, 7, 3, 5]]) \
		== [[1, 0, 3, 0, 5], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [8, 0, 5, 0, 1], [5, 0, 7, 0, 5]], "Error"

	#tests is_rotation function
	assert is_rotation("waterbottle", "erbottlewat") == True, "Error"
	assert is_rotation(None, None) == False, "Error"
	assert is_rotation("", "") == False, "Error"
	assert is_rotation("davidweinberger", "weinbergerdavid") == True, "Error"
	assert is_rotation("rebeccaweinberger", "weinbergerdavid") == False, "Error"	

	#passed
	print "All tests passed."

if __name__ == '__main__':
	main()