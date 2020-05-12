'''
Please write a program to output a random number, which is divisible by 5 and 7, 
between 10 and 150 inclusive using random module and list comprehension.
'''

import random

def Ex71():
    return random.choice([x for x in range(10,151) if x%7 == x%5 == 0])

if __name__ == "__main__":
    print(Ex71())
    