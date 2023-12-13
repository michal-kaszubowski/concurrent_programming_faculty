import random
import sys
from custom_thread import ThreadWithReturnValue

def split_array_into_n_parts(array, array_size, parts_number=2):
    avg = array_size / parts_number
    out = []
    last = 0.0

    while last < array_size:
        out.append(array[int(last):int(last + avg)])
        last += avg

    return out

def generate_array_of_random_integers(array_size, minimal_value=1, maximal_value=9):
    out = []

    for _ in range (0, array_size):
        random_integer = random.randint(minimal_value, maximal_value)
        out.append(random_integer)
    
    return out

def sum_an_array_of_numbers(array, array_size, acc=0):
    if array_size > 1:
        return sum_an_array_of_numbers(array[1:], array_size - 1, acc + array[0])
    else:
        return acc + array[0]

def main():
    sys.setrecursionlimit(10**9)
    array_size = 10000
    threads_amount = 5

    numbers_to_sum = generate_array_of_random_integers(array_size)
    operation_arrays = split_array_into_n_parts(numbers_to_sum, array_size, threads_amount)

    threads_array = []
    for each_array in operation_arrays:
        thread = ThreadWithReturnValue(target=sum_an_array_of_numbers, args=(each_array, len(each_array)))
        thread.start()
        threads_array.append(thread)
    
    result = 0
    for each_thread in threads_array:
        result += each_thread.join()
    
    print("Calculated value:", result)


if __name__ == "__main__":
    main()

