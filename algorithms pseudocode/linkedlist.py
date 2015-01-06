#!/usr/bin/python
#contains pseudocode for various linkedlist operations

"""

class singlylinkedlist:
	self.head = None

	def get_head(self):
		return self.head

	#def insert():
	#def remove():
	#etc...


class singlylinkedlistnode:
	self.next = None
	self.data = None

	def get_next(self):
		return self.next

	def set_next(self, node):
		self.next = node

	def get_data(self):
		return self.data

	def set_data(self, data):
		self.data = data

"""

def reverse_list(linkedlist):
	cur = linkedlist.get_head()
	if not cur:
		return None
	nxt = cur.get_next()
	while nxt:
		temp = nxt.get_next()
		nxt.set_next(cur)
		cur = nxt
		nxt = temp
	return cur
