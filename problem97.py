'''
You are given an integer, N. Your task is to print an alphabet rangoli of size N. 
(Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

----c
--c-b
c-b-a

--------e
------e-d
--e-d-c-b
e-d-c-b-a

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

'''

import string

def str_ptr(string):
    rev = string[::-1]
    return ''.join((string, rev[1:]))

def list_ptr(list):
    rev = list[::-1]
    list = list + rev[1:]
    return list

def Ex98():
    raw_input = int(input())
    alphabet = list(string.ascii_uppercase)
    alphabet = alphabet[:raw_input]
    print(alphabet)
    line_lengh = '-'*(raw_input*2 - 1)
    line_lenght = str(line_lengh)

    even_num = [x for x in range(len(line_lenght)+1) if x%2 == 0]
    print(even_num)
    line_list = []
    
    for char in [0]:
        pass

if __name__ == "__main__":
    Ex98()