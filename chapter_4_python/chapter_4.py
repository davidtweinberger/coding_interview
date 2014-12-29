#!/usr/bin/python
import random
import chapter_3 as c3
import math
import re

#David Weinberger (12/23/2014)
#Note - functions, variables and attributes with the "_" prefix should be treated as
#private and not part of the external API for these data structures.

"""
Answers to the questions in chapter 4 of Cracking the Coding Interview, in Python
Includes my implementations of a Binary Search Tree.

David Weinberger (12/22/2014)
Brown University '16
davidtweinberger@gmail.com 
"""

"""
Binary Search Tree Node

This class represents an encapsulated node with private data fields
to be used in a Binary Tree or a Binary Search Tree.  Accessors and
Mutators are given to avoid the need to directly access instance 
attributes.
"""
class BTNode:
	def __init__(self, value = None, parent=None, lchild=None, rchild=None, depth=None):
		"""
		Inits with any combination of the four optional arguments:
			value : the value of the node, or None
			parent : the parent of the node, or None
			lchild : the left child of the node, or None
			rchild : the right child of the node, or None
			depth : an optional field to keep track of the depth of a node
		"""
		self._value = value
		self._parent = parent
		self._lchild = lchild
		self._rchild = rchild
		self._depth = depth
	def __str__(self):
		return "Node (" + str(self._value) +  ")"

	""" Accessors """
	def value(self):
		return self._value
	def parent(self):
		return self._parent
	def lchild(self):
		return self._lchild
	def rchild(self):
		return self._rchild
	def depth(self):
		return self._depth

	""" Mutators - value defaults to None """
	def setvalue(self, value=None):
		self._value = value
	def setparent(self, parent=None):
		self._parent = parent
	def setlchild(self, lchild=None):
		self._lchild = lchild
	def setrchild(self, rchild=None):
		self._rchild = rchild
	def setdepth(self, depth=None):
		self._depth = depth

	def islchild(self):
		"""
		Returns True if the node instance is a left child,
		False otherwise.  Returns False if the node is a root.
		"""
		if (self.parent() and self.parent().lchild() is self): #TODO is or == here
			return True
		return False

"""
Binary Search Tree

This class represents a binary search tree.
Data can be added, removed and searched. Also supports type checking for data.
Does not contain duplicate data.
See inline comments and docstrings for more information. 

"""
class BST:
	def __init__(self, rootData=None, treetype=None):
		"""
		Inits a new BT instance with an optional root node 
		created with the provided data.
		"""
		self._root = BTNode(rootData) if rootData else None
		self._size = 1 if rootData else 0
		self._treetype = treetype

		#Only for printing functionality
		self._depth = 1 if rootData else 0 #Root is at depth 1
		self._max_chars = len(str(rootData)) if rootData else 1 #max string length of data elements

	def __str__(self):
		"""
		Traverses and prints the binary tree in an organized and pretty way.
		Uses a BFS traversal.
		"""
		self._synchronize_attributes()
		s = ""
		queue = c3.Queue()
		level = 0
		queue.enqueue((1, self._root))
		while queue.peek():
			nodelev, node = queue.dequeue()._data
			if (not node):

				#NODE IS NOT THERE - just a placeholder
				#print spacing and enqueue fake left and right children
				#but stops if they would be past the max depth of the tree
				if ((self._depth - nodelev + 1) <= 0):
					continue

				if (nodelev != level):
					s += "\n"
					#PRINT THE INDENT
					indent = " "*int((self._max_chars)*(2**(self._depth - nodelev) - 1))
					s += indent
					level = nodelev

				#PRINT THE SPACING
				s += " "*(self._max_chars)*(2**(self._depth - nodelev + 1) - 1)

				#PRINT SPACES TO REPLACE DATA
				s += " "*self._max_chars

				#Enqueue fake children
				queue.enqueue((nodelev + 1, None))
				queue.enqueue((nodelev + 1, None))
				continue

			if (nodelev != level):
				s += "\n"
				#PRINT THE INDENT
				indent = " "*(self._max_chars)*(2**(self._depth - nodelev) - 1)
				s += indent
				level = nodelev

			#adds preceding "|"s if the str length of the data is smaller than the max
			for i in range(int(self._max_chars - len(str(node.value())))):
				s += "|"
			s += str(node.value()) 

			#PRINT THE SPACING
			spacing = " "*(self._max_chars)*(2**(self._depth - nodelev + 1) - 1)
			s += spacing

			#Enqueues
			if node.lchild():
				queue.enqueue((nodelev + 1, node.lchild()))
			else:
				#ENQUEUES A FAKE NODE IN ORDER TO FORMAT THE TREE FOR MISSING NODES
				queue.enqueue((nodelev + 1, None))
			if node.rchild():
				queue.enqueue((nodelev + 1, node.rchild()))
			else:
				#ENQUEUES A FAKE NODE IN ORDER TO FORMAT THE TREE FOR MISSING NODES
				queue.enqueue((nodelev + 1, None))
		s += "\n"
		return s

	def clear(self):
		"""
		Completely clears the tree.
		"""
		self._root = None
		self._size = 0
		self._depth = 0
		self._max_chars = 1
		return

	def print_nodes(self, s):
		"""
		Concatenates and prints the nodes in BFS order
		"""
		return ' '.join((s.replace("\n"," ")).split())

	def make_tree(self, l):
		"""
		Adds data from a list to the tree.
		"""
		for el in l:
			self.insert(el)

	def root(self):
		"""
		Returns the root item of the tree, or None if the
		tree is empty.
		"""
		return self._root

	def treetype(self):
		"""
		Returns the type of the tree, or None if the tree 
		is not typed.
		"""
		return self._treetype

	def is_empty(self):
		"""
		Returns True if the tree is empty, else False.
		"""
		return (self._size == 0)

	def _recursive_insert(self, data, node):
		"""
		Traverses and inserts data into the correct place in the tree.
		"""

		#NOTE - this line prevents inserting duplicate data into the tree
		#another alternative is to create a list at each node holding the duplicates
		if (data == node.value()):
			return

		if (data < node.value()):
			if node.lchild():
				self._recursive_insert(data, node.lchild())
			else:
				node.setlchild(BTNode(value=data, parent=node, depth=node.depth() + 1))
		else:
			if node.rchild():
				self._recursive_insert(data, node.rchild())
			else:
				node.setrchild(BTNode(value=data, parent=node, depth=node.depth() + 1))

	def insert(self, data):
		"""
		Inserts an instance of data into the tree.  Raises a 
		TypeError if the data is not the correct type.
		"""

		if (self.treetype() and type(data) != self.treetype()):
			raise TypeError(str(type(data)) + " is invalid for this tree.")

		self._size += 1

		if (not self._root):
			self._root = BTNode(value=data, depth=1)
			return

		self._recursive_insert(data, self._root)
		return

	def remove(self, data):
		"""
		Removes the data from the tree and returns it, else None
		"""
		result = self._recursiveSearch(data, self._root)
		if (result):
			data = self._internalRemove(result)
			self._size -= 1
			return data
		return None

	def _internalRemove(self, node):
		"""
		Removes a node from the data structure and returns its data
		TODO: test this more
		"""
		if not node:
			return None

		#Case 1 - node is a leaf
		if (not node.lchild() and not node.rchild()):
			print str(node.value()) + ": 1"
			if (node is self._root):
				self._root = None
				return node.value()
			if node.islchild():
				node.parent().setlchild()
			else:
				node.parent().setrchild()
			return node.value()

		#Case 2 - node has only 1 child
		if (bool(node.lchild()) != bool(node.rchild())): #basically an XOR
			print str(node.value()) + ": 2"
			if node.lchild():
				if (node is self._root):
					self._root = node.lchild()
					return node.value()
				else:
					if node.islchild():
						node.parent().setlchild(node.lchild())
					else:
						node.parent().setrchild(node.lchild())
					return node.value()
			else:
				if (node is self._root):
					self._root = node.rchild()
					return node.value()
				else:
					if node.islchild():
						node.parent().setlchild(node.rchild())
					else:
						node.parent().setrchild(node.rchild())
					return node.value()

		#case 3 - node has 2 children
		#find minimum element in right subtree, switch data
		#delete the node that had the minimum element
		if (node.lchild() and node.rchild()):
			print str(node.value()) + ": 3"
			minele = node.rchild()
			while minele.lchild():
				minele = minele.lchild()
			temp = node.value()
			node.setvalue(minele.value())
			minele.setvalue(temp)
			self._internalRemove(minele)
			return node.value()

	def purge(self, purgefn=None):
		""" 
		(Only for testing - doesn't always work reliably?)

		This function purges the tree of all nodes for which the data of
		the node satisfies some function purgefn.  Defaults to 
		checking the data type vs. the treetype if there is a treetype, or None
		if there is not.
		"""
		if (not purgefn):
			if (self._treetype):
				purgefn = lambda d : type(d) != self._treetype
			else:
				return None

		#TODO inefficient right now
		data = self.preorder_traverse_to_list()
		data = filter(purgefn, data)

		print "Purging data: " + str(data)

		for ele in data:
			self._internalRemove(self._purgeNode(ele))

	def _purgeNode(self, data):
		"""
		Returns a node with data specified by searching the entire tree.
		(not efficient at all)
		"""
		q = c3.Queue()
		q.enqueue(self._root)
		while q.peek():
			node = q.dequeue()._data
			if node.value() == data:
				return node
			if node.lchild():
				q.enqueue(node.lchild())
			if node.rchild():
				q.enqueue(node.rchild())
		return None

	def _synchronize_attributes(self):
		"""
		Need to do this before print-ing (weird/bad
		random things can happen if you don't).
		Updates tree depth, max_chars, and size vars
		Also updates node depth fields --> need this for the printing to be formatted correctly.
		Also clears unnecessary local attributes from nodes: (not terribly necessary tbh)
			_is_balanced
			_isvalidBST
			_max
			_min
		Uses a BFS traversal.  Assumes self._root is accurate.
		Does not change the treetype, but checks if elements are of the incorrect type.
		"""
		self._depth = 0
		self._max_chars = 1
		self._size = 0
		if (not self._root):
			return
		attrs = ["_is_balanced", "_isvalidBST", "_max", "_min"]
		queue = c3.Queue()
		queue.enqueue((1, self._root))
		while queue.peek():
			nodelev, node = queue.dequeue()._data
			self._size += 1
			if (self._treetype and type(node.value()) != self._treetype):
				#print "WARNING: Tree has been corrupted with data of the wrong type. " \
				#	+ str(type(node.value())) + ": " + str(node.value())
				pass
			for attr in attrs:
				if hasattr(node, attr):
					delattr(node, attr)
			node.setdepth(nodelev)
			if (nodelev > self._depth):
				self._depth = nodelev
			if (len(str(node.value())) > self._max_chars):
				self._max_chars = len(str(node.value()))
			if (node.lchild()):
				queue.enqueue((nodelev + 1, node.lchild()))
			if (node.rchild()):
				queue.enqueue((nodelev + 1, node.rchild()))		

	def _recursiveSearch(self, data, node):
		"""
		Recursively searches the tree for the data
		returns the node, or None
		"""
		if (not node):
			return None
		if (node.value() == data):
			return node
		elif (data < node.value()):
			return self._recursiveSearch(data, node.lchild())
		else:
			return self._recursiveSearch(data, node.rchild())
		

	def search(self, data):
		"""
		Returns data of node with specified data in the tree, or None.
		"""
		result = self._recursiveSearch(data, self._root)
		if (result):
			return result.value()
		return None

	def is_balanced(self, threshold=1):
		"""
		Returns True if the tree is balanced within some threshold.
		False otherwise.
		Uses a recursive postorder traversal.
		"""
		self._recursive_postorder(self._root, threshold)
		return self._root._is_balanced

	def _recursive_postorder(self, node, threshold):
		"""
		A recursive postorder traversal beginning at the node specified.
		Uses an _is_balanced decoration to keep track.
		"""
		ltree = 0
		rtree = 0
		if node.lchild():
			ltree = self._recursive_postorder(node.lchild(), threshold)
		if node.rchild():
			rtree = self._recursive_postorder(node.rchild(), threshold)
		if abs(ltree - rtree) > threshold:
			node._is_balanced = False
		else:
			node._is_balanced = True
		return ltree + rtree + 1

	def make_minheight_tree(self, l, isSorted=True):
		"""
		Given a list of (unique) integer elements, creates a BST with minimal height
		Uses an in-place recursive helper function.
		isSorted is whether or not the list is sorted to begin with.
		"""
		if (not l or len(l) == 0):
			return
		self.clear()
		if (not isSorted):
			l = sorted(list(set(l)))
		self._root = self._recursive_minheight(start=0, end=(len(l)-1), l=l, parent=None)
		return None

	def _recursive_minheight(self, start, end, l, parent):
		"""
		Recursive helper function to construct a min-height tree from a list
		Arguments are the start index, the end index, the list to be used,
		and the parent (usually going to be None.)
		(The list contains data or value elements.)
		"""
		#base case - 0, 1 elements left in the list
		if (end < start):
			return None
		if (end == start):
			return BTNode(value=l[end], parent = parent)

		#split list in half and returns
		mid = start + (end-start)/2
		midnode = BTNode(value=l[mid], parent=parent)
		midnode.setlchild(self._recursive_minheight(start, mid-1, l, midnode))
		midnode.setrchild(self._recursive_minheight(mid+1, end, l, midnode))
		return midnode

	def make_linked_lists(self):
		"""
		Makes linked lists of all of the nodes at each depth level in the tree.
		Uses a BFS traversal, for simplicity just uses a list of lists (same as 
		a linked list of linked lists basically)
		"""
		if self.is_empty():
			return []

		queue = c3.Queue()
		lists = [] #an empty list of lists
		level = 0
		queue.enqueue((1, self._root))
		while queue.peek():
			nodelev, node = queue.dequeue()._data
			if (nodelev != level):
				level = nodelev
				lists.append([]) #appends a new empty list for the next level of nodes
			lists[-1].append(node.value())
			if node.lchild():
				queue.enqueue((nodelev + 1, node.lchild()))
			if node.rchild():
				queue.enqueue((nodelev + 1, node.rchild()))
		return lists

	def is_bst(self):
		"""
		Returns True if the instance is a valid binary search tree, False 
		otherwise (if it has been corrupted).
		Uses a recursive postorder traversal.
		"""
		try:
			self._recursive_is_bst_helper(self._root)
		except AttributeError:
			return False
		return self._root._isvalidBST

	def _recursive_is_bst_helper(self, node):
		"""
		Recursive function to traverse the tree and determine if it is a 
		valid binary search tree.  Sort of complicated... 
		An easier way to to this is to do an inorder traversal and 
		see if it's sorted.
		"""
		#base case
		if (not node.lchild() and not node.rchild()):
			node._isvalidBST = True
			node._max = node.value()
			node._min = node.value()
			return

		#do the left and right children
		if (node.lchild()):
			self._recursive_is_bst_helper(node.lchild())
		if (node.rchild()):
			self._recursive_is_bst_helper(node.rchild())

		#update max - max of left max, right max, and node value
		node._max = max(node.lchild()._max if node.lchild() else 0, \
			max(node.rchild()._max if node.rchild() else 0, node.value()))

		#update min - min of left min, right min, and node value
		node._min = min(node.lchild()._min if node.lchild() else float("inf"), \
			min(node.rchild()._min if node.rchild() else float("inf"), node.value()))

		#invalid if left child is invalid
		if (node.lchild() and not node.lchild()._isvalidBST):
			node._isvalidBST = False
			return

		#invalid if right child is invalid
		if (node.rchild() and not node.rchild()._isvalidBST):
			node._isvalidBST = False
			return		

		#invalid if left child is greater than or equal to this node
		if (node.lchild() and node.lchild().value() >= node.value()): 
			self._isvalidBST = False
			return

		#invalid if right child is less than this node
		if (node.rchild() and node.rchild().value() < node.value()): 
			node._isvalidBST = False
			return

		#invalid if left max is greater than or equal to node value
		if (node.lchild() and node.lchild()._max >= node.value()):
			node._isvalidBST = False
			return

		#invalid if right min is less than node value
		if (node.rchild() and node.rchild()._min < node.value()):
			node._isvalidBST = False
			return

		#otherwise it's valid!
		node._isvalidBST = True
		return

	def find_successor(self, node=None, data=None):
		"""
		Finds the in-order successor of a node (or data)
		in the tree, and returns the data of the successor.
		"""
		if ((node == None and data == None) or (node != None and data != None)):
			return None

		if (node == None):
			node = self._recursiveSearch(data, self.root())
			if (node == None):
				return None

		if (node.rchild()):
			successor = node.rchild()
			while successor.lchild():
				successor = successor.lchild()
			return successor

		successor = node
		while not successor.islchild():
			if not successor.parent():
				return None
			successor = successor.parent()
		successor = successor.parent()
		return successor

	def find_common_ancestor(self, node1=None, node2=None, data1=None, data2=None):
		"""
		Function to find the nearest ancestor of two nodes.
		Returns the ancestor node, or None if none exists
		Takes in either two nodes or two data objects to find.
		"""
		#error checking
		if ((bool(node1) != bool(node2)) or (bool(data1) != bool(data2))):
			return None
		if (not node1 and not node2 and not data1 and not data2) or \
			(node1 and node2 and data1 and data1):
			return None

		#search for data
		if (data1!=None):
			node1 = self._recursiveSearch(data1, self.root())
			if not node1:
				return None
		if (data2!=None):
			node2 = self._recursiveSearch(data2, self.root())
			if not node2:
				return None

		#this updates the _depth field of all of the nodes (just in case)
		self._synchronize_attributes()

		#brings nodes to the same depth level
		while (node1.depth() > node2.depth()):
			node1 = node1.parent()
		while (node2.depth() > node1.depth()):
			node2 = node2.parent()

		while (node1 != node2):
			node1 = node1.parent()
			node2 = node2.parent()
			if (not node1 or not node2):
				return None
		return node1

	def preorder_traverse_to_list(self):
		"""
		This function serializes the tree by returning a list with 
		data elements and None instances ordered using a preorder traversal. 
		None values are stored to reflect when a node is 
		missing from the tree.
		"""
		if (not self.root()):
			return None
		self._synchronize_attributes()
		return self._preorder_traverse_to_list_helper(self.root(), 1)

	def _preorder_traverse_to_list_helper(self, node, depth):
		"""
		Helper function for the preorder traversal.
		Returns a list representing the data in the graph rooted at node.
		"""
		#visit node
		l = []
		if (node):
			l.append(node.value())
		else:
			l.append(None)

		#anon function for this thing
		fakechild = lambda:self._preorder_traverse_to_list_helper(None, depth + 1)

		#call on children
		if (node):
			if (node.lchild()):
				l += self._preorder_traverse_to_list_helper(node.lchild(), depth + 1)
			else:
				if (depth < self._depth):
					#recurse with None for empty children (lchild)
					l += fakechild()
			if (node.rchild()):
				l += self._preorder_traverse_to_list_helper(node.rchild(), depth + 1)
			else:
				if (depth < self._depth):
					#recurse with None for empty children (rchild)
					l += fakechild()
		else:
			if (depth < self._depth):
				#recurse with None for empty children (lchild) and (rchild)
				#l += fakechild() #need to call twice?
				l += fakechild()
		return l

	def subtree_matching(self, subtree):
		"""
		Returns a list of nodes at which a subtree matching the subtree
		specified is contained in this tree instance.  Or an empty list if 
		no instances of the subtree in this instance were found.
		"""
		#TODO implement this in a faster way
		text = self.preorder_traverse_to_list()
		pattern = subtree.preorder_traverse_to_list()

		print text
		print pattern

		matches = []
		for i in range(len(text)):
			if text[i:i+len(pattern)] == pattern:
				matches.append(i)
		return matches

	"""TODO MAYBE USE THIS for linear runtime"""
	def KnuthMorrisPratt(self, text, pattern):
		# build table of shift amounts
		shifts = [1 for i in range(len(pattern) + 1)]
		shift = 1
		for pos in range(len(pattern)):
			while shift <= pos and pattern[pos] != pattern[pos-shift]:
				shift += shifts[pos-shift]
			shifts[pos+1] = shift
	 
		# do the actual search
		results = []
		startPos = 0
		matchLen = 0
		for c in text:
			while matchLen == len(pattern) or \
				  matchLen >= 0 and pattern[matchLen] != c:
				startPos += shifts[matchLen]
				matchLen -= shifts[matchLen]
			matchLen += 1
			if matchLen == len(pattern):
				results += [startPos]

		return results
	"""TODO MAYBE USE THIS"""

	def inorder_traverse_to_list(self):
		"""
		This function serializes the tree by returning a list with 
		data elements and None instances ordered using an inorder traversal. 
		"""
		if (not self.root()):
			return None
		self._synchronize_attributes()
		return self._inorder_traverse_to_list_helper(self.root())

	def _inorder_traverse_to_list_helper(self, node):
		"""
		Helper function for the preorder traversal.
		Returns a list representing the data in the graph rooted at node.
		"""
		l = []
		if (node.lchild()):
			l += self._inorder_traverse_to_list_helper(node.lchild())
		l.append(node.value())
		if (node.rchild()):
			l += self._inorder_traverse_to_list_helper(node.rchild())
		return l

def main():
	"""tree = BST(treetype=int)
	tree.make_tree([50, 25, 75, 33, 47, 97, 38, 62, 96, 72, 28, 52, 85, 16, 14])
	print tree
	print tree.is_balanced()

	tree.clear()
	tree.make_minheight_tree(range(28))

	#this messes up the tree
	tree._recursiveSearch(25, tree.root()).setvalue("a")
	print tree

	print tree.make_linked_lists()

	print tree.is_bst()

	print tree.find_successor(data=12)

	print "\n"*10

	print tree.find_common_ancestor(data1=14, data2=23)

	tree.clear()

	tree.make_minheight_tree(range(10))

	print tree

	print "\n"*10

	print tree.preorder_traverse_to_list()

	subtree = BST(treetype=int)

	subtree.make_minheight_tree(range(4))

	print subtree.preorder_traverse_to_list()

	print tree.KMP_for_subtree_matching(subtree)"""

	"""
	tree = BST(treetype=int)
	subtree=BST(treetype=int)

	tree.make_minheight_tree(range(15))

	subtree.make_minheight_tree(range(7))

	print tree 
	print subtree

	print tree.subtree_matching(subtree)
	"""

if __name__ == '__main__':
	main()
