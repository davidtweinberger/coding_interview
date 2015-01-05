#!/usr/bin/python
import random

"""
Answers to the questions in chapter 2 of Cracking the Coding Interview, in Python
Includes my implementations of unsorted and sorted linked lists as well as solutions 
and test cases for the coding problems.

David Weinberger (12/21/2014)
Brown University '16
davidtweinberger@gmail.com 
"""

"""
UNSORTED SINGLY LINKED LIST

Basic unsorted singly-linked list with next 
pointers and a data field at each node
"""
class singly_linked_list:
	def __init__(self):
		#inits instance vars
		self._head = None

	def __str__(self):
		s = ""
		s += "(Head) --> "
		curr = self._head
		while (curr):
			s += curr.tostring()
			s += " --> "
			curr = curr._next
		s += "(End of list)"
		return s

	def clear(self):
		"""
		Clears the list by pointing the head to None if it isn't already.
		"""
		if self._head:
			self._head = None
		return None

	def construct_from_list(self, l):
		"""
		Inserts data elements from list l into the class instance.
		Returns the head of the list, or None if invalid input.
		"""
		if not l:
			return None
		for datum in l:
			self.insert(datum)
		return self._head

	def make_list(self):
		"""
		Constructs and returns a list with the data from the nodes in
		the class instance as distinct list elements.  Returns [] for invalid input
		"""
		if not self._head:
			return []

		l = []
		curr = self._head
		while (curr):
			l.append(curr._data)
			curr = curr._next
		return l

	def insert(self, data):
		"""
		Inserts data in a new node at the end of the list
		Returns the new node, or None if invalid input
		"""

		if (data == None):
			#invalid input
			return None
		if (not self._head):
			#creates the first node in the list
			self._head = singly_linked_list_node(data=data)
			return self._head
		#traverses to the end of the list
		curr = self._head
		while (curr._next):
			curr = curr._next
		curr._next = singly_linked_list_node(data=data)
		return curr._next

	def insert_front(self, data):
		"""
		Inserts data in a new node at the beginning of the list
		and updates the head pointer of the list.  Returns the new 
		node, or None if invalid data.
		"""
		if (data == None):
			return None #invalid input

		#previous head
		temp = self._head

		#updates the head with a new node
		self._head = singly_linked_list_node(data=data, nxt=temp)

		#returns the new head of the list
		return self._head

	def remove(self, data):
		"""
		Removes and returns the first node with the given data from the list
		or None if the node was not found
		"""
		curr = self._head
		#checks for bad input
		if (not curr or data == None):
			return None

		#head is to be deleted
		if (self._head._data == data):
			temp = self._head
			self._head = self._head._next
			return self._head

		#traverses to the node before the one to be deleted
		while (curr._next and curr._next._data != data):
			curr = curr._next

		#reached the end without finding the node
		if (not curr._next):
			return None

		#deletes the next node
		temp = curr._next
		curr._next = curr._next._next

		#returns the deleted node
		return curr._next

	def search(self, data):
		"""
		Searches for and returns the node with the given data
		or returns None if the data was not found in any node
		"""
		curr = self._head
		#checks for bad input
		if (not curr or data == None):
			return None

		#traverses the list
		while (curr and curr._data != data):
			curr = curr._next

		#end of the list was reached
		if not curr:
			return None

		#data was found within the curr node
		return curr

	def reverse(self):
		"""
		Reverses the linked list in-place and returns the new head, 
		or None if invalid input
		"""
		#curr and prev pointers
		curr = self._head
		prev = None

		#error checking
		if curr == None:
			return None

		#iterates through list and updates pointers
		while (curr and curr._next):

			#temp is two nodes after the current one
			temp = curr._next._next

			#sets the next node's next pointer back to the curr node
			curr._next._next = curr

			#temp variable for the prev node
			prev_temp = curr._next

			#sets the curr node's next variable to be the prev node
			curr._next = prev

			#updates prev
			prev = prev_temp

			#updates curr
			curr = temp

		if curr:
			#last node next pointer
			curr._next = prev

			#updates head pointer
			self._head = curr
			return self._head

		else:
			#even number of nodes means curr is None at the end of the traversal
			self._head = prev
			return self._head

	def remove_duplicates(self):
		"""
		Removes all duplicate elements in the list.  Returns the head
		of the list, or None if invalid input.  Uses a set() to keep track.
		"""
		#curr is used to traverse the list
		curr = self._head

		#check for bad input
		if not curr:
			return None

		#inits a set
		nodes = set()
		nodes.add(curr._data)

		#traverses through nodes starting with head, examining the next node's data 
		#to see if it has already been visited.
		while (curr._next):
			
			#update the next node while the next node's data is already in the set
			while (curr._next and curr._next._data in nodes):
				curr._next = curr._next._next

			#add data to the set
			if curr._next and curr._next._data:
				nodes.add(curr._next._data)
			
			#update the curr pointer
			curr = curr._next
			
			#breaks if the end of the list has been reached
			if not curr:
				break

		#returns the head
		return self._head

	def kth_to_last(self, k):
		"""
		Finds and returns the kth to last node in a singly linked list
		or None if invalid input or such a node does not exist in the given list.
		Uses the runner technique of a secondary pointer to remove the need to 
		know the exact number of items in the list.
		"""
		#two pointers used to iterate
		curr = self._head
		kth = self._head

		if not curr or (k == None):
			return None

		for i in range(int(k)):
			curr = curr._next
			if not curr:
				#not enough nodes in the list
				return None

		#iterates until curr has reached the end of the list
		while (curr._next):
			curr = curr._next
			kth = kth._next

		#kth is k nodes behind curr
		return kth

	def remove_node(self, node):
		"""
		Removes a node from the middle of the linked list given access only 
		to that node.  Returns the node removed, or None if invalid input.
		"""

		#invalid input
		if not node:
			return None

		#if node is the first one, need to update the head pointer
		if node == self._head:
			self._head = node._next
			return node

		#if node is the last one, cannot remove it only given a pointer to it.
		if not node._next:
			return None

		#otherwise, copy the data in the node from the next node,
		#and then delete the next node
		tempdata = node._next._data
		node._next._data = node._data
		node._data = tempdata

		#deletes the next node
		temp = node._next
		node._next = node._next._next

		#returns the node that is being deleted
		return node._next

	def partition(self, val, cmpfn=lambda x, y:1 if x < y else 0):
		"""
		Function that partitions (reorders) a linked list such that all nodes 
		with data less than val come before all nodes with data greater to 
		or equal to val.  Returns head of the list, or None if invalid input.
		Optional argument is a comparison function used to compare data elements.
		Note that this implementation is not stable (ordering is not preserved)
		A stable implementation would use two auxiliary lists and merge them at the end.

		Example:
			1 -> 5 -> 2 -> 9 -> 1 -> 3 -> 8 ->2 	with val = 3 might become
			1 -> 2 -> 1 -> 2 -> 5 -> 9 -> 3 -> 8
		"""

		#error checking
		curr = self._head
		if (not curr or val==None):
			return None

		#creates a new list
		new_list = singly_linked_list()

		#iterates through the list, adding elements either to the front or back of the new list
		while (curr):
			#data is less than val -> insert at the front
			if cmpfn(curr._data, val): 
				new_list.insert_front(curr._data)
			else:
				new_list.insert(curr._data)
			curr = curr._next

		#returns the partitioned list
		return new_list

	def is_partitioned(self, val, cmpfn=lambda x, y:1 if x < y else 0):
		"""
		Function that returns True if a list is partitioned around a value
		(val) as described above.  Returns False otherwise.  Optional 
		argument is a comparison function used to compare data elements.
		"""
		
		#error checking
		curr = self._head
		if (not curr or val==None):
			return False

		#traverses through list until the first element equal or greater to 
		#val is found.  Then returns False if an element smaller than val is
		#found before the end of the list, else True.
		while (cmpfn(curr._data, val)):
			curr = curr._next

			#reached the end of the list before finding an element >= val
			if not curr:
				return True

		while (not cmpfn(curr._data, val)):
			curr = curr._next

			#reached the end of the list before finding an element < val
			if not curr:
				return True

		#found an element that was smaller than val after one that was = to or greater
		return False

	def int_from_list(self):
		"""
		Function that transforms a linked list of digits (in reverse order) 
		into an integer and returns that integer, or None if an error occurred.
		Assumes that the list is a list of integers in [0, 10).
		"""

		#error checking
		curr = self._head
		if (not curr):
			return None

		#traverses through the list
		curr_pow = 1
		num = 0
		while(curr):
			#invalid
			if ((curr._data > 9) or (curr._data < 0)):
				return None 
			num += curr._data*curr_pow
			curr_pow *= 10
			curr = curr._next

		#returns the sum
		return num

	def list_from_int(self, i):
		"""
		Function to be performed on an empty list - adds each digit from the integer
		i in reverse order to the list.  Returns the head of the new list or None
		"""

		#error checking
		if (i == None):
			return None

		#constructs a new list - sort of cheating but it's ok
		digits = [int(d) for d in reversed(str(i))]
		self.construct_from_list(digits)
		return self._head

	def find_loop_start(self):
		"""
		Finds the start of the loop in a linked list, and returns that node, 
		or None for invalid input or if there is not a loop.
		Note - not that efficient in terms of space, uses an auxiliary set. (TODO)
		"""

		#error checking
		curr = self._head
		if not curr:
			return None

		#adds nodes to a set
		nodes = set()

		#traverses
		while (curr):
			if curr in nodes:
				return curr
			else:
				nodes.add(curr)
			curr = curr._next

		#reached the end of the list, no cycle
		return None

	def is_palindrome(self):
		"""
		Returns True if a linked list is a palindrome, False otherwise.
		Note that this algorithm uses an auxiliary list (TODO)
		"""

		#error checking
		curr = self._head
		if not curr:
			return False

		#iterates, adds nodes to a stack
		stack = []
		while (curr):
			stack += [curr._data]
			curr = curr._next

		#iterates and checks to see if reverse is the same as forwards
		curr = self._head
		while (curr):
			if stack.pop(-1) != curr._data:
				return False
			curr = curr._next

		#returns True if all data is the same backwards and forwards
		return True

class singly_linked_list_node:
	def __init__(self, data=None, nxt=None):
		#inits instance vars
		self._data = data
		self._next = nxt
	
	#overwrites the default print method
	def __str__(self):
		return "Singly-linked list node with data: " + self.tostring()

	#returns the data in the node as a string
	def tostring(self):
		return str(self._data)


"""
SORTED SINGLY LINKED LIST

A sorted singly linked list composed of nodes with next pointers and data fields.

Args:
	cmpfn = a comparison function (defaults to the ">" operator)
	isequal = an equality function (defaults to the == operator).

Create a list in decreasing order simply by using cmpfn=lambda x, y: 1 if x > y else 0
Change the isequal function to change the conditions for when two data instances are considered equal.
"""
class sorted_list:
	def __init__(	
					self, 
					cmpfn = 	lambda x, y: 1 if x < y else 0, 
					isequal = 	lambda x, y: 1 if x == y else 0
				): 
		#inits instance vars
		self._head = None
		self._cmpfn = cmpfn
		self._isequal = isequal

	def __str__(self):
		s = ""
		s += "(Head) --> "
		curr = self._head
		while (curr):
			s += curr.tostring()
			s += " --> "
			curr = curr._next
		s += "(End of list)"
		return s

	def clear(self):
		"""
		Clears the list by pointing the head to None if it isn't already.
		"""
		if self._head:
			self._head = None
		return None

	def construct_from_list(self, l):
		"""
		Inserts data elements from list l into the class instance.
		Returns the head of the list, or None if invalid input.
		"""
		if not l:
			return None
		for datum in l:
			self.insert(datum)
		return self._head

	def make_list(self):
		"""
		Constructs and returns a list with the data from the nodes in
		the class instance as distinct list elements.  Returns [] for invalid input
		"""
		if not self._head:
			return []

		l = []
		curr = self._head
		while (curr):
			l.append(curr._data)
			curr = curr._next
		return l

	def insert(self, data):
		"""
		Traverses the linked list starting with self._head and finds the first element
		in the list that is greater than or equal to the data passed in (the first element 
		for which the comparator function returns 0).  It then inserts a new node before
		the first node that is greater than or equal to the given data.  Returns the new 
		node or None if invalid data.
		"""
		#curr will be used to iterate
		curr = self._head

		#check for bad input
		if (data == None):
			return None

		#head is being inserted (list was empty)
		if (not curr):
			self._head = sorted_list_node(data=data)
			return self._head

		#head is being updated (data is smaller than the previous head)
		if not self._cmpfn(curr._data, data):
			prev_head = self._head
			self._head = sorted_list_node(data=data, nxt=prev_head)
			return self._head

		#traverses while data is smaller than curr._next._data
		while (curr._next and self._cmpfn(curr._next._data, data)):
			curr = curr._next

		#curr is either the last node smaller than data or the last node
		next_node = curr._next
		curr._next = sorted_list_node(data=data, nxt=next_node)
		return curr._next

	def insert_without_duplicate(self, data):
		"""
		Inserts a new node with the specified data into the list in the correct place if
		the data does not already exist within the list. (A very slight modification to the
		above function.) Returns the new node, or None if invalid or duplicate data.
		"""
		#curr will be used to iterate
		curr = self._head

		#check for bad input
		if (data == None):
			return None

		#head is being inserted (list was empty)
		if (not curr):
			self._head = sorted_list_node(data=data)
			return self._head

		#head is being updated (data is smaller than the previous head)
		if not self._cmpfn(curr._data, data):
			if not self._isequal(curr._data, data):
				prev_head = self._head
				self._head = sorted_list_node(data=data, nxt=prev_head)
				return self._head
			return None

		#traverses while data is smaller than curr._next._data
		while (curr._next and self._cmpfn(curr._next._data, data)):
			curr = curr._next

		#curr is either the last node smaller than data or the last node
		if ((not curr._next) or (curr._next and not self._isequal(curr._next._data, data))):
			next_node = curr._next
			curr._next = sorted_list_node(data=data, nxt=next_node)
			return curr._next

		#duplicate data
		return None

	def remove(self, data):
		"""
		Removes the first node with the data specified.  Returns this node, or 
		None if the data was not found in the list.
		"""
		#curr will be used to iterate
		curr = self._head

		#check for bad input
		if (not curr or data == None):
			return None

		#head is being removed (list head is updated to the next node)
		if self._isequal(curr._data, data):
			prev_head = curr
			self._head = prev_head._next
			return prev_head

		#traverses the list until 
		#1. node with matching data is found, 
		#2. data is smaller than the current node (data not found in list),
		#3. curr is the last node in the list
		while (curr._next 
			and not self._isequal(curr._next._data, data) 
			and self._cmpfn(curr._next._data, data)):
			curr = curr._next

		#reached end of the list
		if not curr._next:
			return None

		#reached a node that has data larger than the data given
		if self._cmpfn(data, curr._next._data):
			return None

		#reached a node with matching data
		curr._next = curr._next._next
		return curr._next

	def search(self, data):
		"""
		Searches the list for the first node with the provided data and 
		returns that node, or None if the data was not found in the list.
		"""

		#curr will be used to iterate
		curr = self._head

		#check for bad input
		if (not curr or data == None):
			return None

		#check if it's the head
		if self._isequal(curr._data, data):
			return curr

		#traverses the list until 
		#1. node with matching data is found, 
		#2. data is smaller than the current node (data not found in list),
		#3. curr is the last node in the list
		while (curr._next 
			and not self._isequal(curr._next._data, data) 
			and self._cmpfn(curr._next._data, data)):
			curr = curr._next

		#reached the end of the list
		if not curr._next:
			return None

		#next node data is greater than the data searching for 
		if self._cmpfn(data, curr._next._data):
			return None

		#otherwise, next node data is equal to the data searching for
		return curr._next

class sorted_list_node:
	def __init__(self, data=None, nxt=None):
		#inits instance vars
		self._data = data
		self._next = nxt

	#overwrites the default print method
	def __str__(self):
		return "Sorted singly-linked list node with data: " + self.tostring()

	#returns the data in the node as a string
	def tostring(self):
		return str(self._data)


#Test cases for problems from chapter 2

def problem_2_1():
	l = singly_linked_list()
	l.construct_from_list([1, 1, 2, 3, 4, 5, 6, 6, 6, 6, 7, 8, 8, 8])
	l.remove_duplicates()
	assert l.make_list() == [1, 2, 3, 4, 5, 6, 7, 8], "Error"

	m = singly_linked_list()
	m.construct_from_list([1, 6, 3, 7, 4, 3, 6, 2, 1, 1, 8, 6, 6, 5, 4])
	m.remove_duplicates()
	assert m.make_list() == [1, 6, 3, 7, 4, 2, 8, 5], "Error"

	n = singly_linked_list()
	n.remove_duplicates()
	assert n.make_list() == [], "Error"

	o = singly_linked_list()
	o.construct_from_list([3, 2, 1, 6, 8, 5, 4, 9, 7])
	o.remove_duplicates()
	assert o.make_list() == [3, 2, 1, 6, 8, 5, 4, 9, 7], "Error"

	o = singly_linked_list()
	o.construct_from_list([1])
	o.remove_duplicates()
	assert o.make_list() == [1], "Error"

def problem_2_2():
	l = singly_linked_list()
	l.construct_from_list([2, 6, 5, 8, 4, 3, 2, 5])
	elem = l.kth_to_last(3)
	assert elem._data == 4, "Error"
	elem = l.kth_to_last(0)
	assert elem._data == 5, "Error"
	elem = l.kth_to_last(7)
	assert elem._data == 2, "Error"
	elem = l.kth_to_last(8)
	assert elem == None, "Error"
	elem = l.kth_to_last(None)
	assert elem == None, "Error"
	l.clear()
	l.construct_from_list([2])
	elem = l.kth_to_last(0)
	assert elem._data == 2, "Error"
	elem = l.kth_to_last(1)
	assert elem == None, "Error"

def problem_2_3():
	l = singly_linked_list()
	l.construct_from_list([2, 6, 5, 8, 5, 5, 3, 1, 7])
	
	node = l.search(3)
	l.remove_node(node)
	assert l.make_list() == [2, 6, 5, 8, 5, 5, 1, 7], "Error"

	node = l.search(6)
	l.remove_node(node)
	assert l.make_list() == [2, 5, 8, 5, 5, 1, 7], "Error"

	node = l.search(10)
	l.remove_node(node)
	assert l.make_list() == [2, 5, 8, 5, 5, 1, 7], "Error"

	node = l.search(5)
	l.remove_node(node)
	assert l.make_list() == [2, 8, 5, 5, 1, 7], "Error"

	node = l.search(7)
	l.remove_node(node)
	assert l.make_list() == [2, 8, 5, 5, 1, 7], "Error"

	node = l.search(2)
	l.remove_node(node)
	assert l.make_list() == [8, 5, 5, 1, 7], "Error"

	node = l.search(5)
	l.remove_node(node)
	assert l.make_list() == [8, 5, 1, 7], "Error"

	l.clear()
	l.construct_from_list([3])
	node = l.search(3)
	l.remove_node(node)
	assert l.make_list() == [], "Error"

def problem_2_4():
	l = singly_linked_list()
	l.construct_from_list([1, 4, 8, 3, 6, 2, 9, 3, 1, 5, 7])
	l = l.partition(4)
	assert l.is_partitioned(4) == True, "Error"

	l.clear()
	l.construct_from_list([1, 4, 8, 3, 6, 2, 9, 3, 1, 5, 7])
	assert l.is_partitioned(4) == False, "Error"

	l = singly_linked_list()
	l.construct_from_list([random.randint(0, 100) for i in range(100)])
	l = l.partition(50)
	assert l.is_partitioned(50) == True, "Error"

	l = singly_linked_list()
	assert l.is_partitioned(5) == False, "Error"
	assert l.is_partitioned(None) == False, "Error"

	l.insert(5)
	assert l.is_partitioned(5) == True, "Error"
	assert l.is_partitioned(0) == True, "Error"
	assert l.is_partitioned(10) == True, "Error"

def problem_2_5():
	l = singly_linked_list()
	m = singly_linked_list()
	l.construct_from_list([7, 1, 6])
	m.construct_from_list([5, 9, 2]) 

	sum_int = l.int_from_list() + m.int_from_list()

	sum_list = singly_linked_list()
	sum_list.list_from_int(sum_int)
	
	assert sum_list.int_from_list() == 912, "Error"

	l.clear()
	m.clear()
	l.construct_from_list([7, 1, 6, 4, 7, 2, 5, 8])
	m.construct_from_list([5, 9, 2, 0, 0, 0, 3]) 

	sum_int = l.int_from_list() + m.int_from_list()

	sum_list = singly_linked_list()
	sum_list.list_from_int(sum_int)
	
	assert sum_list.int_from_list() == 88274912, "Error"

def problem_2_6():
	l = singly_linked_list()
	l.construct_from_list(range(10))
	l.search(9)._next = l.search(7)
	assert l.find_loop_start() == l.search(7), "Error"

	l.clear()
	l.construct_from_list(range(500))
	assert l.find_loop_start() == None, "Error"

	l.clear()
	l.construct_from_list(range(500))
	l.search(463)._next = l.search(244)
	assert l.find_loop_start() == l.search(244), "Error"

	l.clear()
	assert l.find_loop_start() == None, "Error"

def problem_2_7():
	l = singly_linked_list()
	l.construct_from_list(range(10))
	l.construct_from_list(reversed(range(10)))
	assert l.is_palindrome() == True, "Error"

	l.clear()
	l.construct_from_list(range(10))
	l.construct_from_list(reversed(range(8)))
	assert l.is_palindrome() == False, "Error"

	l.clear()
	l.construct_from_list([1])
	assert l.is_palindrome() == True, "Error"

	l.clear()
	assert l.is_palindrome() == False, "Error"

	l.clear()
	l.construct_from_list(range(500))
	assert l.is_palindrome() == False, "Error"

def reverse():
	l = singly_linked_list()
	l.construct_from_list(range(20))
	l.reverse()

def main():
	problem_2_1()
	problem_2_2()
	problem_2_3()
	problem_2_4()
	problem_2_5()
	problem_2_6()
	problem_2_7()
	reverse()
	print "All tests passed."

if __name__ == '__main__':
	main()