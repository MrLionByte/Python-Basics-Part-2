#Write a Python function set_intersection that takes two sets and returns their intersection.
# The function should return a new set containing only the elements that are present in both input sets.

def set_intersection(input1: set, input2:set) -> set:
    input1,input2 = list(input1),list(input2)
    new_set = set()
    for i in input1:
        if i in input2:
            new_set.add(i)

    return new_set

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result = set_intersection(set1, set2)
print(result) 

# more efficient approach for above is :O(1)
def set_intersection(set1: set, set2: set) -> set:
    return set1 & set2

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result = set_intersection(set1, set2)
print(result)

