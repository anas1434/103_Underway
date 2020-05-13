'''
Please write a program to randomly generate a list with 5 numbers, 
which are divisible by 5 and 7 , between 1 and 1000 inclusive.
'''

import random

def Ex75():
    raw_list = []
    for x in range(5):
        raw_list.append(random.choice([y for y in range(1,1001) if y%5==y%7==0]))
    return raw_list

if __name__ == "__main__":
    print(Ex75())
