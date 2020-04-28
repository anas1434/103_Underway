'''
Write a program which can filter() to make a list whose elements are 
even number between 1 and 20 (both included).
'''

from problem42 import Ex42

def Ex43(num):
    return Ex42(num)

if __name__ == "__main__":
    print(list(filter(Ex43, list(range(21)))))