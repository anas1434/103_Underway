'''
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

Suppose the following input is supplied to the program:

Hello world!
Then, the output should be:

UPPER CASE 1
LOWER CASE 9
'''

import string

def Ex14():
    upper_case = list(string.ascii_uppercase)
    lower_case = list(string.ascii_lowercase)
    no_uc = 0
    no_lc = 0
    raw_input = input()
    for char in raw_input:
        if char in upper_case:
            no_uc+=1
        elif char in lower_case:
            no_lc+=1
        else:
            pass
    return f"UPPER CASE {no_uc}\nLOWER CASE {no_lc}"

if __name__ == "__main__":
    print(Ex14())