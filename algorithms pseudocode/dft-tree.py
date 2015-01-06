#! /usr/bin/python

#doesn't check if nodes have been visited already (need to do that for a graph traversal to avoid infinite loops)
#THIS IS PSEUDOCODE

def dft(root): #same as preorder
	S = stack()
	S.push(root)
	while not S.isEmpty():
		node = S.pop()
		visit(node)
		S.push(node.left())
		S.push(node.right())

#recursive implementations
#called from another method with the root node as the argument


def preorder(node):
	visit(node)
	if node.left():
		preorder(node.left())
	if node.right():
		preorder(node.right())

def inorder(node):
	if node.left():
		inorder(node.left())
	visit(node)
	if node.right():
		inorder(node.right())

def postorder(node):
	if node.left():
		postorder(node.left())
	if node.right():
		postorder(node.right())
	visit(node)