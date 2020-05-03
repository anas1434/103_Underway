'''
The Fibonacci Sequence is computed based on the following formula:

f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1

Please write a program to compute the value of f(n) with a given n input by console.

Example: If the following n is given as input to the program:

7

Then, the output of the program should be:

13
'''

def Ex61():
    num = int(input())
    def fib(num):
        if num == 0:
            return 0
        elif num == 1:
            return 1
        else:
            return fib(num - 1) + fib(num -2)
    return fib(num)

if __name__ == "__main__":
    print(Ex61())