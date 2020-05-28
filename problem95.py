'''
Given the participants' score sheet for your University Sports Day, 
you are required to find the runner-up score. You are given scores. 
Store them in a list and find the score of the runner-up.

If the following string is given as input to the program:

5
2 3 6 6 5

Then, the output of the program should be:

5
'''

def Ex95():
    #raw_input = int(input())
    raw_list = map(int, input().split())
    raw_list = list(set(raw_list))
    print(raw_list[-2])

if __name__ == "__main__":
    Ex95()
