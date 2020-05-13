'''
Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.
'''

import random

def Ex72():
    raw_list = []
    for x in range(5):
        raw_list.append(random.choice(list(range(100,201))))
    return raw_list

if __name__ == "__main__":
    print(Ex72())
