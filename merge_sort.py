import random
from tqdm import tqdm
from utils import test_sort


def merge_sort(unsorted):
	n = len(unsorted)
	if n <= 1:
		return unsorted
	else:
		a = merge_sort(unsorted[0:n//2])
		b = merge_sort(unsorted[n//2:])
		i=0
		j=0
		c = []
		for k in range(n):
			if i >= len(a):
				c.append(b[j])
				j += 1
			elif j >= len(b):
				c.append(a[i])
				i += 1
			elif a[i] <= b[j]:
				c.append(a[i])
				i += 1
			elif a[i] > b[j]:
				c.append(b[j])
				j += 1
		return c


if __name__ == "__main__":
	n = 100000
	unsorted_list = [random.randint(0, 1000) for i in range(n)]

	sorted_list = merge_sort(unsorted_list)
	test_sort(sorted_list)

