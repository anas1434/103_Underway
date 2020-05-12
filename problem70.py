'''
Please write a program to output a random even number between 0 and 10 
inclusive using random module and list comprehension.
'''

import random

def Ex70():
    return random.choice([x for x in range(11) if x%2==0])

if __name__ == "__main__":
    print(Ex70())
    