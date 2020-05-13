'''
Please write a program to print the running time of execution of "1+1" for 100 times.
'''

import time

def Ex77():
    
    before = time.time()
    for x in range(1001):
        a = 1+1
    after = time.time()
    time_taken = after - before
    print(time_taken)

if __name__ == "__main__":
    Ex77()
