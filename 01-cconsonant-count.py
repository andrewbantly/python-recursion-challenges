'''
Write a function that given a string, counts total number of consonants in it. 
A consonant is a English alphabet character that is not vowel (a, e, i, o and u). 
Examples of constants are b, c, d, f, g, ..
input will never have spaces or non letter characters

Examples: 

Input: 'snakes'
Output: 4

Input: 'SpamAndEggs'
Output: 8
'''

def print_consonants(word, index=0):
    consonants = 0
    vowels = ["a", "e", "i", "o", "u"]
    # base case 
    if index == len(word):
        return 0
    # logic 
    if word[index].lower() not in vowels:
        consonants += 1
    # invoke recursion 
    return consonants + print_consonants(word, (index + 1))


print(print_consonants("SpamAndEggs"))