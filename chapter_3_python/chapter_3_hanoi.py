#!/usr/bin/python

import chapter_3 as c3
import copy

"""
An implementation of the "Towers of Hanoi" Game implemented using my own Stack 
class and a simple recursive solution.

David Weinberger (12/22/2014)
Brown University '16
davidtweinberger@gmail.com 
"""

class HanoiGame:
	"""
	Args:
		num: 		The number of discs to use
		startpole: 	The starting pole [1-3]
		endpole: 	The ending pole [1-3]
		wait: 		Waits after each move for user to press return in the terminal

	Prints out each step of the game, just to show what's going on.
	"""
	def __init__(self, num=4, startpole=0, endpole=2, wait=False):
		#init instance vars
		self._num = num
		self._stacks = [c3.Stack() for i in range(3)]
		self._wait = wait
		self._moves = 0

		#error checking with start/end poles
		if (startpole < 0 or startpole > 2 or endpole < 0 
		or endpole > 2 or startpole == endpole):
			startpole = 0
			endpole = 2
			print "Warning: invalid poles chosen."

		self._startpole = startpole
		self._endpole = endpole

		#inits the first stack (discs represented as integers)
		for i in range(int(num)):
			self._stacks[self._startpole].push(num - i)

	def __str__(self):
		#code to print a simple representation of the game
		ret = "Number of moves: " + str(self._moves) + "\n"
		for i in range(3):
			cp = copy.deepcopy(self._stacks[i])
			l = cp.reduce_to_list()
			s = "|-"
			for disc in l:
				s += str(disc)
				s += "-"
			s += "\n"
			ret += s
		return ret

	def get_game_attributes(self):
		"""
		Returns the attributes of the game formatted as a tuple:
		(num, startpole, endpole)
		"""
		return (self._num, self._startpole, self._endpole)

	def is_over(self):
		"""
		Returns True if the game is over, False otherwise.
		"""
		cp = copy.deepcopy(self._stacks[self._endpole])
		l = cp.reduce_to_list()
		return l == list(reversed([i + 1 for i in range(self._num)]))

	def do_move(self, num, src, dest):
		"""
		Code to perform the next move for the game
		"""

		if (num == 1):
			self.switch(src, dest)
		else:
			other = self.other_pole(src, dest)
			self.do_move(num-1, src, other)
			self.switch(src, dest)
			self.do_move(num-1, other, dest)
		return 

	def switch(self, p1, p2):
		"""
		Code to move the top disc from one pole to the top of another pole
		"""
		self._stacks[p2].push(self._stacks[p1].pop()._data)
		self._moves += 1
		print self
		if (self._wait): raw_input()
		return 

	def other_pole(self, p1, p2):
		"""
		Returns the other pole (the one that is not specified with the args)
		"""
		poles = [0, 1, 2]
		poles.remove(p1)
		poles.remove(p2)
		return poles[0]

def main():
	game = HanoiGame(num=5, wait=False)
	print "Initial State:"
	print game
	if (game._wait): raw_input()

	num, src, dest = game.get_game_attributes()
	game.do_move(num, src, dest)

	print "Final State"
	print game

if __name__ == '__main__':
	main()