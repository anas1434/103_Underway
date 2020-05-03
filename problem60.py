'''
Write a program to compute:

f(n)=f(n-1)+100 when n>0

and f(0)=0

with a given n input by console (n>0).

Example: If the following n is given as input to the program:

5

Then, the output of the program should be:

500

In case of input data being supplied to the question, it should be assumed to be a console input.
'''

def Ex60():
    num = int(input())
    def func(num):
        
        if num == 0:
            return 0
        return func(num-1) + 100
    return func(num)
    

if __name__ == "__main__":
    print(Ex60())