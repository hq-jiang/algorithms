from tqdm import tqdm
from utils import test_sort, random_list

def insertion_sort(unsorted):
	'''
	Worst case O(n^2)
	Best case O(n)
	'''
	for i in xrange(len(unsorted)):
		if i==0:
			continue
		a = unsorted[i]
		for j in reversed(range(i)):

			if a >= unsorted[j] and j==i-1:
				break
			elif a < unsorted[j] and j==0:
				del unsorted[i]
				unsorted.insert(j,a)
				break
			elif a < unsorted[j]:
				continue
			elif a >= unsorted[j]:
				del unsorted[i]
				unsorted.insert(j+1,a)
				break
		
	return unsorted


if __name__ == "__main__":
	n = 10000
	unsorted_list = random_list(n,1000)

	sorted_list = insertion_sort(unsorted_list)
	test_sort(sorted_list)
