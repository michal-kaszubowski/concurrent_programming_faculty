import time
from prime_functions import *

def main():
    left = 1000000
    right = 2000000
    print(left, ":", right)
    start = time.time()
    result = get_primes_in_range(left, right)
    end = time.time()
    print(result)
    print(">>", end-start)


if __name__ == '__main__':
    main()

