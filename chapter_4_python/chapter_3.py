#!/usr/bin/python

import random
import time

"""
Answers to the questions in chapter 3 of Cracking the Coding Interview, in Python
Includes my implementations of Stack and Queue data structures, as well as some
other creative data structures and explorations of object-oriented python.

David Weinberger (12/22/2014)
Brown University '16
davidtweinberger@gmail.com 
"""

#function to get the current time in milliseconds
current_time_milliseconds = lambda: int(round(time.time()*1000))

"""
NODE 

This is a simple node class used in the Stack and the Queue classes.
"""
class Node:
	def __init__(self, data=None, nxt=None, minimum=None):
		#inits instance vars
		self._data = data
		self._next = nxt
		self._min = minimum
	
	#overwrites the default print method
	def __str__(self):
		return "Node with data: " + self.tostring()

	#returns the data in the node as a string
	def tostring(self):
		return str(self._data)

"""
STACK

This is a simple stack implemented using a linked list of nodes.
Also has a min() function that returns the value of the min data 
element currently in the stack (in O(1) time).
"""
class Stack:
	def __init__(self):
		#inits instance vars
		self._head = None
		self._items = 0

	def __str__(self):
		s = ""
		s += "(Top of Stack) --> "
		curr = self._head
		while (curr):
			s += curr.tostring()
			s += " --> "
			curr = curr._next
		s += "(Bottom of Stack)"
		return s

	def is_empty(self):
		"""
		Returns True if the instance is empty, else False
		"""
		return self._items == 0

	def clear(self):
		"""
		Clears the stack by pointing the head to None if it isn't already.
		Returns the stack.
		"""
		if self._head:
			self._head = None
		return self

	def construct_from_list(self, l):
		"""
		Pushes data elements from list l into the class instance.
		Returns the stack, or None if invalid input.
		"""
		if not l:
			return None
		for datum in l:
			self.push(datum)
		return self

	def reduce_to_list(self):
		"""
		Exports the data elements contained in the stack to a list.
		The list is ordered with the bottom of the stack first, and the 
		top of the stack last.
		Warning - destroys the original stack. (can be reconstructed
		with the above function, however.)
		Returns the list, or [] if the stack was empty to begin with.
		"""
		l = []
		while (self.peek()):
			l.append(self.pop()._data)
		return reversed(l)

	def push(self, data, specify_min=None):
		"""
		Pushes a new node with the specified data onto the top of the stack.
		Returns the node, or None if invalid input.
		"""

		#invalid input
		if (data == None):
			return None 

		#previous head
		temp = self._head

		#updates the head with a new node
		if not specify_min:
			minval = min(temp._min, data) if temp else data
		else:
			minval=min(specify_min, data)
		self._head = Node(data=data, nxt=temp, minimum=minval)

		#increments counter
		self._items += 1

		#returns the stack
		return self._head

	def pop(self):
		"""
		Pops the first node off of the top of the stack.
		Returns the node, or None if there wasn't one.
		"""

		#invalid input
		if not self._head:
			return None

		#decrements counter
		self._items -= 1

		#updates the head and returns the old head
		temp = self._head
		self._head = self._head._next
		return temp

	def peek(self):
		"""
		Returns the data in the first node in the stack, or None.
		"""

		#invalid input
		if not self._head:
			return None

		return self._head._data

	def min(self):
		"""
		Returns the min value currently in any of the nodes in the stack.
		or None if the stack is empty.
		"""
		if not self._head:
			return None

		return self._head._min

	def sort(self):
		"""
		Sorts the stack in ascending order (with biggest items on top)
		Uses 1 additional stack. Returns the stack instance.
		"""
		auxiliary = Stack()

		#pours into auxiliary
		while not self.is_empty():
			auxiliary.push(self.pop()._data)

		#puts elements back into self in sorted order
		while not auxiliary.is_empty():
			curr = auxiliary.pop()._data
			if self.is_empty():
				self.push(curr)
				continue
			count = 0
			while (self.peek() > curr):
				auxiliary.push(self.pop()._data)
				count += 1
			self.push(curr)
			for i in range(count):
				self.push(auxiliary.pop()._data)

		return self

"""
QUEUE

This is a simple queue implemented using a linked list of nodes.
"""
class Queue:
	def __init__(self):
		#inits instance vars
		self._head = None
		self._tail = None

	def __str__(self):
		s = ""
		s += "(Start of Queue) --> "
		curr = self._head
		while (curr):
			s += curr.tostring()
			s += " --> "
			curr = curr._next
		s += "(End of Queue)"
		return s

	def clear(self):
		"""
		Clears the queue by pointing the head to None if it isn't already
		and the same for the tail.  Returns the Queue.
		"""
		if self._head:
			self._head = None
		if self._tail:
			self._tail = None
		return self

	def construct_from_list(self, l):
		"""
		Enqueues data elements from list l into the class instance.
		Returns the queue, or None if invalid input.
		"""
		if not l:
			return None
		for datum in l:
			self.enqueue(datum)
		return self

	def enqueue(self, data):
		"""
		Enques a new node with the specified data onto the end of the queue.
		Returns the node, or None if invalid input.
		"""

		#error checking
		if (data == None):
			return None

		#only element in the queue, update both head and tail
		if (self._head == None):
			new = Node(data=data, nxt=None)
			self._head = new
			self._tail = new
			return new

		#queue already had at least one element
		self._tail._next = Node(data=data, nxt=None)
		self._tail = self._tail._next
		return self._tail

	def dequeue(self):
		"""
		Dequeues the first node of the queue, and returns that node, if there
		is one.  Otherwise returns None.
		"""

		#error checking - queue is empty
		if (not self._head):
			return None

		#returns the previous head, and updates the head pointer and tail pointer if necessary
		temp = self._head
		self._head = self._head._next
		if (not self._head):
			self._tail = None
		return temp

	def peek(self):
		"""
		Returns the data in the first node in the queue, or None.
		"""

		#invalid input
		if not self._head:
			return None

		return self._head._data

"""
SET OF STACKS

This class represents a data structure composed of multiple stacks.
Each stack can contain only a certain number of items at a time.  If 
that number is exceeded, a new internal stack is created.  The push, pop,
peek and min operations as well as clear() and construct_from_list() are 
still supported and function exactly the same as with the normal Stack.

Args:
	threshold: 	an optional threshold value specifying the max items per stack.
				defaults to a value of 10.
"""
class SetOfStacks:
	def __init__(self, threshold=10):
		#init instance vars here
		self._threshold = threshold
		self._stacks = [Stack()]

	def __str__(self):
		ret = ""
		for i, stack in enumerate(self._stacks):
			s = "Stack " + str(i) + ". "
			s += "(Top of Stack) --> "
			curr = stack._head
			while (curr):
				s += curr.tostring()
				s += " --> "
				curr = curr._next
			s += "(Bottom of Stack)\n"
			ret += s
		return ret

	def construct_from_list(self, l):
		"""
		Pushes data elements from list l into the class instance.
		Returns the SetOfStacks, or None if invalid input.
		"""
		if not l:
			return None
		for datum in l:
			self.push(datum)
		return self

	def push(self, data):
		"""
		Pushes a new node with data onto the current stack in the set of stacks, 
		and then creates a new empty stack if necessary.
		"""
		#current stack is the last one in the list
		curr_stack = self._stacks[-1]

		#pushes a new node - specifying the minimum value comparison as necessary 
		#to preserve the correct min values for the nodes
		if (curr_stack._items == 0) and (len(self._stacks) > 1):
			curr_min = self._stacks[-2].min()
			new = curr_stack.push(data, specify_min=curr_min)
		else:
			new = curr_stack.push(data)

		#check if the stack is full
		if curr_stack._items == self._threshold:
			self._stacks.append(Stack())

		#returns
		return new

	def pop(self):
		"""
		Pops and returns the last node added to the set of stacks, or None.
		"""
		#gets the current stack
		curr_stack = self._stacks[-1]

		#checks if empty, if so, pops the empty stack and sets curr_stack to the next one
		#unless there is nothing in the set of stacks
		if (curr_stack._items == 0):
			if (len(self._stacks) > 1):
				self._stacks.pop()
				curr_stack = self._stacks[-1]
			else:
				return None

		#pops from the current stack and returns
		return curr_stack.pop()

	def peek(self):
		"""
		Returns the data element in the last node added to the set of stacks, or None.
		"""
		#gets the current stack
		curr_stack = self._stacks[-1]

		#the current stack might be empty
		if (curr_stack._items == 0):
			if (len(self._stacks) > 1):
				curr_stack = self._stacks[-2]
			else:
				return None

		#peeks from the current stack and returns
		return curr_stack.peek()

	def min(self):
		"""
		Returns the min data element of all nodes in the set of stacks, or None.
		"""

		#gets the current stack
		curr_stack = self._stacks[-1]

		#the current stack might be empty
		if (curr_stack._items == 0):
			if (len(self._stacks) > 1):
				curr_stack = self._stacks[-2]
			else:
				return None

		#peeks from the current stack and returns
		return curr_stack.min()

"""
MyQueue - A Queue that is implemented using two stacks
"""
class MyQueue:
	def __init__(self):
		#inits instance vars
		self._stack = Stack()
		self._auxiliary = Stack()

	def enqueue(self, data):
		"""	
		Enqueue just enqueues the data onto the stack
		"""
		self._stack.push(data)

	def dequeue(self):
		"""
		Dequeue "pours" the stack into the auxiliary (reversing the order)
		and pops from the auxiliary, then pours back into the stack.
		"""
		while not self._stack.is_empty():
			self._auxiliary.push(self._stack.pop()._data)
		temp = self._auxiliary.pop()
		while not self._auxiliary.is_empty():
			self._stack.push(self._auxiliary.pop()._data)
		return temp

"""
DogCatQueue

See problem 3.7 in the book for details.
Uses two Queue instances to solve the problem.
"""
class DogCatQueue:
	def __init__(self):
		self._dogQueue = Queue()
		self._catQueue = Queue()
		self._count = 0
	def __str__(self):
		s = "DogQueue:\n"
		s += str(self._dogQueue)
		s += "\nCatQueue:\n"
		s += str(self._catQueue)
		s += "\n"
		return s

	"""
	Enqueues a new animal onto the correct stack
	"""
	def enqueue(self, animal):
		if (not animal):
			return
		if isinstance(animal, Dog):
			self._dogQueue.enqueue(DogCatQueue.AnimalNode(animal, self._count))
			self._count += 1
		elif isinstance(animal, Cat):
			self._catQueue.enqueue(DogCatQueue.AnimalNode(animal, self._count))
			self._count += 1
		return 

	"""
	Dequeues and returns a Cat, if there is one, else returns None.
	"""
	def dequeueCat(self):
		node = self._catQueue.dequeue()
		if (node):
			catnode = node._data
			cat = catnode._animal
			return cat

	"""
	Dequeues and returns a Dog, if there is one, else returns None.
	"""
	def dequeueDog(self):
		node = self._dogQueue.dequeue()
		if (node):
			dognode = node._data
			dog = dognode._animal
			return dog

	"""
	Dequeues and returns the oldest animal of any type, if there is one
	otherwise returns None.
	"""
	def dequeueAny(self):
		dogPeek = self._dogQueue.peek()
		catPeek = self._catQueue.peek()
		if (dogPeek and catPeek):
			if (dogPeek._time < catPeek._time):
				node = self._dogQueue.dequeue()
				dognode = node._data
				dog = dognode._animal
				return dog
			else:
				node = self._catQueue.dequeue()
				catnode = node._data
				cat = catnode._animal
				return cat	
		elif (dogPeek and (not catPeek)):
			node = self._dogQueue.dequeue()
			dognode = node._data
			dog = dognode._animal
			return dog
		elif ((not dogPeek) and catPeek):
			node = self._catQueue.dequeue()
			catnode = node._data
			cat = catnode._animal
			return cat
		else:
			#no animals left :(
			return None

	"""
	Inner class representing the node containing an Animal instance (
	either a Dog or a Cat) and a timestamp for when the node was added.
	"""
	class AnimalNode:
		#node inits with animal instance and timestamp (actually just a counter)
		def __init__(self, animal, time):
			self._animal = animal
			self._time = time
		def __str__(self):
			s = ""
			s += "<Cat> " if isinstance(self._animal, Cat) else "<Dog> "
			s += "\""+str(self._animal._name)+"\" "
			s += "(time = " + str(self._time) + ")"
			return s

"""
Classes representing the animals held in this data structure.
Superclass Animal (with name attribute) and Dog/Cat subclasses
"""
class Animal:
	def __init__(self, name):
		self._name = name
		pass

class Dog(Animal):
	def __init__(self, name):
		Animal.__init__(self, name)
		pass

class Cat(Animal):
	def __init__(self, name):
		Animal.__init__(self, name)
		pass

def main():
	DCQueue = DogCatQueue()
	DCQueue.enqueue(Dog("A the dog"))
	DCQueue.enqueue(Dog("B the dog"))
	DCQueue.enqueue(Cat("C the cat"))
	print DCQueue
	DCQueue.dequeueAny()
	DCQueue.dequeueAny()
	DCQueue.dequeueAny()
	print DCQueue
	DCQueue.enqueue(Dog("X the dog"))
	DCQueue.enqueue(Cat("Y the cat"))
	DCQueue.enqueue(Dog("Z the dog"))
	print DCQueue
	DCQueue.dequeueDog()
	DCQueue.dequeueCat()
	DCQueue.dequeueAny()
	print DCQueue

if __name__ == '__main__':
	main()
