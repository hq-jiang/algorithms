import matplotlib.pyplot as plt
from merge_sort import merge_sort
import random
from tqdm import tqdm
import time


def benchmarking(sort_func):
	benchmark_times = []
	n_list = [] 
	for i in tqdm(range(150)):
		n = 1000*(i+1)
		unsorted_list = [random.randint(0, n) for i in range(n)]
		tic = time.clock()
		sorted_list = sort_func(unsorted_list)
		benchmark_times.append(time.clock()-tic)
		n_list.append(n)
	return n_list, benchmark_times

n_list, benchmark_times = benchmarking(merge_sort)

plt.figure()
plt.plot(n_list, benchmark_times)
plt.show()