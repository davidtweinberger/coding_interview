#! /usr/bin/python

#doesn't check if nodes have been visited already (need to do that for a graph traversal to avoid infinite loops)
#THIS IS PSEUDOCODE

def bft(root):
	Q = Queue()
	Q.enqueue(root);
	while not Q.isEmpty():
		node = Q.dequeue()
		visit(node)
		Q.enqueue(node.left())
		Q.enqueue(node.right())