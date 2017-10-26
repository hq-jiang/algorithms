import matplotlib.pyplot as plt
from merge_sort import merge_sort
from insertion_sort import insertion_sort
import random
from tqdm import tqdm
import time
from utils import random_list


def benchmarking(sort_func):
	benchmark_times = []
	n_list = []

	#expected_time
	#for i in range(150):
	#	n = 1000*(i+1)

	tic = time.clock()
	for i in tqdm(xrange(150)):
		n = 1000*(i+1)
		unsorted_list = random_list(n,n)
		tic2 = time.clock()
		sorted_list = sort_func(unsorted_list)
		benchmark_times.append(time.clock()-tic2)
		n_list.append(n)
	print 'Passed time:', time.clock()-tic
	return n_list, benchmark_times


n_list, benchmark_times = benchmarking(sorted)

plt.figure()
ax = plt.gca()
ax.set_xlim([0,160000])
ax.set_ylim([0,1.5])
plt.title('Python Built-in Sort')
plt.plot(n_list, benchmark_times)
plt.savefig('./doc/built_in_sort.png', bbox_inches='tight')
plt.show()

