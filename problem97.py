'''
You are given an integer, N. Your task is to print an alphabet rangoli of size N. 
(Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

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

def Ex98():
    raw_input = int(input())
    alphabet = list(string.ascii_uppercase)
    alphabet = alphabet[:raw_input]
    line_lenght = '-'*(raw_input*4 - 3)
    line_list = []
    for x in range(raw_input):
        line_list.append(line_lenght)
    print(line_list)

if __name__ == "__main__":
    Ex98()