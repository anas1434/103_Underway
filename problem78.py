'''
Please write a program to shuffle and print the list [3,6,7,8].
'''

from random import shuffle

def Ex78():
    raw_list = [3,6,7,8]
    shuffle(raw_list)
    print(raw_list)

if __name__ == "__main__":
    Ex78()
    