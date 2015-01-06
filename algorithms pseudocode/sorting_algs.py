#!/usr/bin/python
import random

def radix_sort(A):
	buckets = [[] for i in range(10)]
	max_digits = len(str(max(A)))
	for i in range(max_digits):
		for num in A:
			if (len(str(num)) > i):
				d = int(str(num)[-i-1])
			else:
				d = 0
			buckets[d].append(num)
		A = reduce(lambda a, b: a + b, buckets)
		buckets = [[] for i in range(10)]
	return A

def quick_sort(A, low, high):
	if low < high:
		pivot_index = partition(A, low, high)
		quick_sort(A, low, pivot_index - 1)
		quick_sort(A, pivot_index + 1, high)
	return A

def partition(A, low, high): #partitions an array between two indices
	pivot_index = random.randint(low, high)
	pivot = A[pivot_index]

	temp = A[pivot_index]
	A[pivot_index] = A[high]
	A[high] = temp

	curr_index = low
	for i in range(low, high):
		if (A[i] <= pivot):
			temp = A[i]
			A[i] = A[curr_index]
			A[curr_index] = temp
			curr_index += 1

	temp = A[high]
	A[high] = A[curr_index]
	A[curr_index] = temp

	return curr_index

def test_sort(array):
	valid = True
	for i in range(1, len(array)):
		if (array[i] < array[i-1]):
			valid = False
			break
	return "is valid. " if valid else "is invalid. "

if __name__ == "__main__":
	array = [random.randint(0, 10000) for i in range(1000)]
	sort = radix_sort(array)
	print "radix sort " + test_sort(sort)

	array = [random.randint(0, 10000) for i in range(1000)]
	sort = quick_sort(array, 0, len(array)-1)
	print "quick sort " + test_sort(sort)








