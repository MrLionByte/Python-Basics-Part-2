# Write a Python generator function find_primes that yields prime numbers one at a time, starting from 2. 
# Implement it in a memory-efficient way without storing all the primes discovered so far.

def find_primes():
    yield 2
    c = 3
    while True:
        is_prime = True
        for i in range(2,int(c**0.5)+1):
            if c%i==0:
                is_prime = False
                break
        if is_prime:
            yield c
        c += 2

value = find_primes()
for i in range(10):
    print(next(value))
