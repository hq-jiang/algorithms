import random

def test_sort(sorted_list):
	prev = sorted_list[0]
	for i in sorted_list:
		if i >= prev:
			prev = i
		else:
			print 'Sorting list failed'
			return False
	print 'Sorting list successful'
	return True

def random_list(n, rng):
	return [random.randint(0, rng) for i in range(n)]
