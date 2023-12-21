import os, errno, threading, math


def split_interval(low, high, size, parts, acc = []):
    end = low + size
    
    if parts > 1:
        return split_interval(end, high, size, parts - 1, acc + [(low, end)])
    
    return acc + [(low, high)]

def is_prime(number):
    if number == 0:
        return False
    
    high = math.ceil(math.sqrt(number))
    for each in range (2, high + 1):
        if number % each == 0:
            return False
    
    return True

def get_primes_in_range(low, high):
    primes = []

    for each in range(low, high):
        if is_prime(each):
            primes.append(each)
    
    return primes

def prime_thread_target(low, high, outoput_queue, barrier):
    # output = os.open(outoput_queue, os.O_WRONLY)
    primes = get_primes_in_range(low, high)
    for each in primes:
        output_data = str(each) + ':'
        os.write(outoput_queue, output_data.encode())
    barrier.wait()

def sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return sort(less)+equal+sort(greater)
    
    return array

def main():
    solutions_queue_key = 'sol_queue'
    
    low = 0
    high = 1000
    threads_amount = 5
    size_of_partition = (high - low) // threads_amount
    partitons = split_interval(low, high, size_of_partition, threads_amount)

    try:
        os.mkfifo(solutions_queue_key)
    except OSError as oe:
        if oe.errno != errno.EEXIST:
            raise
    
    solutions_queue = os.open(solutions_queue_key, os.O_RDWR)

    barrier = threading.Barrier(threads_amount)

    for i in range(0, len(partitons)):
        each = partitons[i]
        thread = threading.Thread(target=prime_thread_target, args=(each[0], each[1], solutions_queue, barrier))
        thread.start()

    barrier.wait()
    os.write(solutions_queue, ';'.encode())

    acc = ''
    primes = []

    while True:
        cell = os.read(solutions_queue, 1).decode()
        if cell == ':' and len(acc) != 0:
            primes.append(int(acc))
            acc = ''
        elif cell == ':' and len(acc) == 0:
            pass
        elif cell == ';':
            break
        else:
            acc = acc + cell

    sorted = sort(primes)
    print(sorted)
    

if __name__ == "__main__":
    main()

