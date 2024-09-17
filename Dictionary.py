#Write a Python function merge_dicts that takes two dictionaries and merges them into one.
# If the same key appears in both dictionaries, the value from the second dictionary should overwrite
# the value from the first dictionary. The function should return the merged dictionary.

#note : PYTHON Inbuilt dict method update override already existing key if both are same.

def merge_dicts(dict1,dict2):
    dict1.update(dict2)
    return dict1

    

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
result = merge_dicts(dict1, dict2)
print(result)  
# Output should be {'a': 1, 'b': 3, 'c': 4}

#Write a Python function merge_dicts that takes two dictionaries and merges them into one.
# If the same key appears in both dictionaries, the value from the first dictionary should overwrite
# the value from the second dictionary. The function should return the merged dictionary.

def merge_dicts(dict1,dict2):
    filtered_dict = {k:v for k,v in dict2.items() if k not in dict1}
    dict1.update(filtered_dict)
    return dict1

    

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
result = merge_dicts(dict1, dict2)
print(result) 

#Write a Python function count_occurrences that takes a list of elements and returns a dictionary where
# the keys are the unique elements from the list, and the values are the counts of those elements in the list.

def count_occurrences(elements: list) -> dict:
    data_dict = {}
    for element in elements:
        if element not in data_dict:
            data_dict[element] = 1
        else:
            data_dict[element] += 1
    return data_dict


elements = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
result = count_occurrences(elements)
print(result)
