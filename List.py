#Write a Python function remove_duplicates that takes a list of integers and removes any duplicates, 
# returning a new list with only unique values while preserving the original order of their first occurrence.

def remove_duplicates(sample_list):
    seen = set()
    unique_list = []
    for i in sample_list:
        if i not in seen:
            unique_list.append(i)
            seen.add(i)
    return unique_list

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))

#THe above approach make sure the data order is not changed since we are using list, while using set to check wether it is repeated is efficient since it's time complexity is O(1)
# while if we use list for this it will become O(n) since it checks whole list each time on each loop.


# ??? Write a Python function find_missing_number that takes a list of integers containing n distinct numbers taken from 0 to n.
# The list contains exactly one number missing from the range. Find and return that missing number.

def find_missing_number(nums):
    size = len(nums)
    expected = size*(size+1)//2
    actual = sum(nums)
    return expected-actual

print(find_missing_number([3,2,4,6, 0, 1]))

# ?? Write a Python function rotate_list that takes a list and an integer k and rotates the list to the right by k steps.
# For example, given [1, 2, 3, 4, 5, 6, 7] and k = 3, the function should return [5, 6, 7, 1, 2, 3, 4].

def rotate_list(nums,k):
    k = k%len(nums)
    return nums[-k:] +nums[:-k]

print(rotate_list( [1, 2, 3, 4, 5, 6, 7],9))

#Write a Python function group_anagrams that takes a list of strings and groups anagrams together.
# The function should return a list of lists, where each inner list contains words that are anagrams of each other.
#Example : group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]).

def group_anagrams(list_words):
    anagrams = {}
    for word in list_words:
        sorted_word = "".join(sorted(word))

        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]

    return list(anagrams.values())
    

x = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(x)