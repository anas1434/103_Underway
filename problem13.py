'''
Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program:

hello world! 123

Then, the output should be:

        LETTERS 10
        DIGITS 3
'''
import string
def Ex13():
    alphabets = list(string.ascii_lowercase)
    alphabets.append(string.ascii_uppercase)
    numbers = list(string.digits)
    raw_input = input()
    no_char = 0
    no_num = 0
    for char in raw_input:
        if char in alphabets:
            no_char+=1
        elif char in numbers:
            no_num+=1
        else:
            pass
    return f"LETTERS {no_char}\nDIGITS {no_num}"

if __name__ == "__main__":
    print(Ex13())