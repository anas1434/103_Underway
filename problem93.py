'''
Please write a program which prints all permutations of [1,2,3]
'''

from itertools import permutations

def Ex93():
    raw_list = [1,2,3]
    for x in list(permutations(raw_list)):
        print(x)

if __name__ == "__main__":
    Ex93()
