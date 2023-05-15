'''
Write a recursive function called reverse that accepts a string and returns a reversed string.

Examples:

input: "computer"
output: "retupmoc"

input: "ab"
output: "ba"

input: "abcdefghijklmnopqrstuvwxyz"
output: "zyxwvutsrqponmlkjihgfedcba"
'''

def reverse_string(word, index=0):
    new_word = ""
    # base case 
    if index == len(word):
        return new_word
    # logic
    new_word += word[index]
    # call the recursive function 
    return reverse_string(word, index + 1) + new_word

print(reverse_string("abcdefghijklmnopqrstuvwxyz"))