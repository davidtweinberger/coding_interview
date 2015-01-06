#! /usr/bin/python

##################################################
# function to return the node with the data toFind, 
# or null if no such node in the tree.
# PSEUDOCODE ONLY

#input: node (the root node), toFind (data to find)

def contains(node, toFind):
	if node.data == toFind:
		return node

	else if toFind < node.data and node.left is not None:
		return contains(node.left, toFind) #searching left subtree

	else if toFind > node.data and node.right is not None:
		return contains(node.right, toFind) #searching right subtree

	return None #no match found


##################################################
# function to insert a node into the BST
# does nothing if data is already in the tree.
# PSEUDOCODE ONLY

#input: node (the root node), toInsert (data to insert)

def insert(node, toInsert):
	if node.data == toInsert:
		return

	if toInsert < node.data
		if node.left is None:
			node.addLeft(toInsert)
		else:
			insert(node.left, toInsert)

	else:
		if node.right is None:
			node.addRight(toInsert)
		else:
			insert(node.right, toInsert)

##################################################
# function to remove a node from the BST
# three cases - leaf, 1 child, 2 children
# PSEUDOCODE ONLY

#input: node (the node to remove - find by calling contains

def remove(node):
	if not node.left or node.right:			#node is a leaf
		node.parent.removeChild(node)

	else if node.left and not node.right:	#only has a left child
		if node.parent.left == node:		#node is a left chilc
			node.parent.left = node.left
		else:
			node.parent.right = node.left

	else if node.right and not node.left:
		if node.parent.left = node:
			node.parent.left = node.right
		else:
			node.parent.right = node.right

	else:
		next_node = successor(node)			#has at most 1 child
		node.data = next_node.data
		remove(next_node)


##################################################
# helper function to find the in-order successor 
# of a node.  Used when removing nodes from a 
# BST.
# PSEUDOCODE ONLY

#input node (a node with both left and right children)

def successor(node):
	succ = node.right
	while (curr.left is not None):
		curr = curr.left
	return curr


#note - can also use the predecessor in place of the successor, can keep the tree more balanced