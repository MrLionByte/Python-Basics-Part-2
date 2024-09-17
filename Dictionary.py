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

