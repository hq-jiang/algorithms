import matplotlib.pyplot as plt
from merge_sort import merge_sort
import random
from tqdm import tqdm
import time


def benchmarking(sort_func):
	benchmark_times = []
	n_list = []

	#expected_time
	#for i in range(150):
	#	n = 1000*(i+1)

	tic = time.clock()
	for i in tqdm(range(150)):
		n = 1000*(i+1)
		unsorted_list = [random.randint(0, n) for i in range(n)]
		tic2 = time.clock()
		sorted_list = sort_func(unsorted_list)
		benchmark_times.append(time.clock()-tic2)
		n_list.append(n)
	print tic - time.clock()
	return n_list, benchmark_times

n_list, benchmark_times = benchmarking(merge_sort)

plt.figure()
plt.title('Merge Sort')
plt.plot(n_list, benchmark_times)
plt.savefig('./doc/merge_sort', bbox_inches='tight')
plt.show()