'''
Please write a program using generator to print the even numbers between 0 and n 
in comma separated form while n is input by console.

Example: If the following n is given as input to the program:

10

Then, the output of the program should be:

0,2,4,6,8,10

In case of input data being supplied to the question, it should be assumed to be a console input.
'''

def Ex63():
    def even_gen():
        num = int(input())
        for n in range(num+1):
            if n%2 == 0:
                yield n
    for number in even_gen():
        print(number, end=',')

if __name__ == "__main__":
    Ex63()
    