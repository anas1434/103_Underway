'''
You are given a string S and width W. Your task is to wrap the string into a paragraph of width.

If the following string is given as input to the program:

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Then, the output of the program should be:

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
'''

from textwrap import wrap

def Ex96():
    raw_input = input()
    width = int(input())
    for text in wrap(raw_input, width):
        print(text)

if __name__ == "__main__":
    Ex96()
