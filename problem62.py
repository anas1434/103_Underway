'''
The Fibonacci Sequence is computed based on the following formula:

f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1

Please write a program to compute the value of f(n) with a given n input by console.

Example: If the following n is given as input to the program:

7

Then, the output of the program should be:

0,1,1,2,3,5,8,13

In case of input data being supplied to the question, it should be assumed to be a console input.
'''

def Ex62():
    num = int(input())
    def fib_list(num = 0, raw_list = []):
        def fib(num):
            if num == 0:
                return 0
            elif num == 1:
                return 1
            else:
                return fib(num - 1) + fib(num -2)
    
        for n in range(num+1):
            if n == 0:
                raw_list.append(fib(0))
            elif n == 1:
                raw_list.append(fib(1))
            else:
                raw_list.append(fib(n - 1) + fib(n -2))
        return (raw_list)
    x = (fib_list(num))
    for item in x:
        print(item, end=',')

if __name__ == "__main__":
    Ex62()