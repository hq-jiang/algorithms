import matplotlib.pyplot as plt
import time
from tqdm import tqdm

def read_file(file_path):
    with open(file_path) as f:
        lines = f.readlines()

        lines = [int(line.strip('\r\n')) for line in lines]
        assert type(lines[0])==int
        assert len(lines)==100000

        return lines

def benchmarking(func, numbers):
    benchmark_times = []
    n_list = []

    tic = time.clock()
    steps = [10, 100, 500, 1000, 5000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
    for n in tqdm(steps):
        tic2 = time.clock()
        sorted_list = func(numbers[:n])
        benchmark_times.append(time.clock()-tic2)
        n_list.append(n)
    print 'Passed time:', time.clock()-tic
    return n_list, benchmark_times

def count_inversions(numbers):
    n = len(numbers)

    if n==1:
        return 0, numbers, []

    # Divide
    a = numbers[:n//2]
    b = numbers[n//2:]
    
    # Conquer
    count_a, merged_a, inv_a= count_inversions(a)
    count_b, merged_b, inv_b= count_inversions(b)

    ### Combine
    count = count_a + count_b
    inversions = inv_a + inv_b

    i_a=0
    i_b=0
    merged = []
    n_a = len(merged_a)
    n_b = len(merged_b)
    for _ in xrange(n):
        if i_a >= n_a:
            merged.append(merged_b[i_b])
            i_b+=1
        elif i_b >= n_b:
            merged.append(merged_a[i_a])
            i_a+=1

        elif merged_a[i_a] <= merged_b[i_b]:
            merged.append(merged_a[i_a])
            i_a += 1
    
        elif merged_a[i_a] > merged_b[i_b] :
            merged.append(merged_b[i_b])
            for j in merged_a[i_a:]:
                inversions.append((j, merged_b[i_b])) 
                count += 1
            i_b += 1
        
    return count, merged, inversions

if __name__=='__main__':
    numbers = read_file('count_inversions.txt')
    numbers = [20,2,5,4,6,9,8,13,12]
    count, sorted_list, inversions = count_inversions(numbers)
    print inversions
    print 'Number of inversions', count
    print sorted_list
    
    #plt.figure()
    #ax = plt.gca()
    #plt.title('Benchmarking Sorting Algorithms')

    #n_list, benchmark_times = benchmarking(count_inversions, numbers)
    #ax.plot(n_list, benchmark_times, label='sorted')
    #plt.savefig('./doc/count_inversions.png', bbox_inches='tight')
    #plt.show()