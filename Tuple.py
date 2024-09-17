# Write a Python function swap_elements that takes a tuple and two indices, and returns a new tuple
# with the elements at those indices swapped. If the indices are out of range, the function should return the original tuple.

def swap_elements(tup: tuple, index1: int, index2: int) -> tuple:
    tup = list(tup)
    tup[index1],tup[index2] = tup[index2],tup[index1]
    return tuple(tup)


tup = (1, 2, 3, 4)
result = swap_elements(tup, 1, 3)
print(result) 

# Write a Python function unpack_tuple that takes a tuple of any length and returns a dictionary where the keys are the
# indices of the elements in the tuple (starting from 0), and the values are the elements themselves.

def unpack_tuple(tup: tuple) -> dict:
    ans = {}
    for i in range(len(tup)):
        ans[i] = tup[i]
    return ans


tup = ('a', 1, True, 3.14)
result = unpack_tuple(tup)
print(result)
