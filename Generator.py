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

#Write a Python generator function fibonacci_generator that yields numbers in the Fibonacci sequence, starting from 0. 
# The generator should be memory-efficient and only store the last two values needed to generate the next number in the sequence.

def fibonacci_generator():
    a,b = 0, 1
    while True:
        yield a
        a,b = b, a+b
    
x = fibonacci_generator()
for i in range(10):
    print(next(x))

#Write a Python generator function even_numbers that yields even numbers starting from 2.
# The generator should be designed to be memory-efficient and should not use a list to store numbers.

def gen_even_numbers():
    ans = 2
    while True:
        yield ans
        ans += 2

x = gen_even_numbers()
for i in range(20):
    print(next(x))

#Write a Python generator function flatten that takes a nested list (a list of lists, which may contain further nested lists) 
# and yields all the elements in a flattened, one-dimensional order.
#For example, given the input [[1, 2, [3, 4]], [5, [6]], 7], the generator should yield 1, 2, 3, 4, 5, 6, 7.

def gen_flatten(x):
    for i in x:
        if isinstance(i, list):
            yield from gen_flatten(i)
        else:
            yield i


x = [[1, 2, [3, 4]], [5, [6]], 7]

for i in gen_flatten(x):
    print(i)
