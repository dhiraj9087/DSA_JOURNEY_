import math

def generate_primes(n):
    """
    Returns a list of the first n prime numbers.
    """
    if n < 1:
        return []
    
    primes = [2]
    num = 3
    while len(primes) < n:
        is_prime = True
        for prime in primes:
            if prime > math.sqrt(num):
                break
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 2
    
    return primes

n =int(input()) # change this to generate the first n prime numbers
primes = generate_primes(n)
for i in primes:
    print(i,end=' ')
# print(primes)

