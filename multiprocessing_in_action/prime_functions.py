import math

def get_max_primes_number_in_range(left, right):
    return math.ceil(6 / 5 * (right - left) / math.log(right - left))

def split_range_into_parts(left, right, size, parts, acc = []):
    end = left + size
    
    if parts > 1:
        return split_range_into_parts(end, right, size, parts - 1, acc + [(left, end)])
    
    return acc + [(left, right)]

def is_prime(number):
    for each in range(2, number - 1):
        if each * each > number:
            return True
        if number % each == 0:
            return False
    return True

def is_prime_with_primes(number, primes):
    for each in primes:
        if number % each == 0:
            return False
        if each * each > number:
            return True
    return True

def get_primes_in_range(left, right):
    small_primes = []
    pivot = math.ceil(math.sqrt(right))

    for each in range (2, pivot + 1):
        if is_prime(each):
            small_primes.append(each)
    
    primes = []

    for each in range(left, right):
        if is_prime_with_primes(each, small_primes):
            primes.append(each)
    
    return primes

