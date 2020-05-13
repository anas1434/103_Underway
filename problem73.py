'''
Please write a program to randomly generate a list with 5 
even numbers between 100 and 200 inclusive.
'''

import random

def Ex73():
    raw_list = []
    for x in range(5):
        raw_list.append(random.choice([y for y in range(100,201) if y%2==0]))
    return raw_list

if __name__ == "__main__":
    print(Ex73())
