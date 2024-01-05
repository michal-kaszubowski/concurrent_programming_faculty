from multiprocessing import Pool, Lock
from multiprocessing.sharedctypes import Array
import time
from prime_functions import *

def print_shared_array():
    for each in range(0, shared_array_size):
        print(shared_array[each], end=", ")

def build_tasks(partitions, number_of_partitions, pivots):
    tasks = []
    
    for each in range(0, number_of_partitions):
        tasks.append([partitions[each][0], partitions[each][1], pivots[each]])
    
    print(tasks)
    return tasks

def do_task(task):
    left = task[0]
    right = task[1]
    pivot = task[2]

    primes = get_primes_in_range(left, right)

    for each in range(0, len(primes)):
        shared_array[pivot + each] = primes[each]

if __name__ == '__main__':
    main_left = 1000000
    main_right = 2000000

    number_of_partitions = 5
    size_of_partition = (main_right - main_left) // number_of_partitions
    partitions = split_range_into_parts(main_left, main_right, size_of_partition, number_of_partitions)
    
    pivot_factor = get_max_primes_number_in_range(partitions[0][0], partitions[0][1])
    pivots = [pivot_factor * each for each in range(0, number_of_partitions)]

    print(pivots)

    lock = Lock()
    shared_array_size = pivots[-1] + pivot_factor
    shared_array = Array('i', shared_array_size, lock=lock)

    tasks = build_tasks(partitions, number_of_partitions, pivots)

    pool = Pool(number_of_partitions)

    start = time.time()
    pool.map(do_task, tasks)
    end = time.time()

    print_shared_array()
    print(">>", end - start)

