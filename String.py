#Write a Python function reverse_words that takes a string as input and returns the string with the words reversed.
# The words in the output should appear in reverse order, but the characters within each word should remain in the original order.

# Example : "hello world this is python" => "python is this world hello"


def reverse_words(words : str):
    temp = (words.split())[::-1]
    words = " ".join(temp)
    return words

print(reverse_words("hello world this is python"))


#Write a Python function find_pair_with_sum that takes a list of integers and a target sum.
# The function should return a tuple of two numbers from the list that add up to the target sum. If no such pair exists, return None.

def find_pair_with_sum(numbers : list,target: int):
    seen = set()
    for number in numbers:
        second_number = target - number
        if second_number in seen:
            return (number,second_number)
        else:
            seen.add(number)
    return

x = find_pair_with_sum([2, 7, 11, 15], 9)
print(x)


#Write a Python function longest_palindromic_substring that takes a string as input and returns the longest palindromic substring within that string.
# If there are multiple substrings of the same maximum length, return the first one found.

def longest_palindromic_substring(word):
    def palindrome_checker(check):
        return check == check[::-1]
    
    longest = ""

    for i in range(len(word)):
        for j in range(i+1,len(word)+1):
            sub_string = word[i:j]
            if palindrome_checker(sub_string) and len(sub_string) > len(longest):
                longest = sub_string

    return longest


palindrome = longest_palindromic_substring("babad")
print(palindrome)