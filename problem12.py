'''
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that 
each digit of the number is an even number.The numbers obtained should be printed in a 
comma-separated sequence on a single line.
'''


values = []
for i in range(1000, 3001):
    if (i%2)==0 and ((i//10)%2)==0 and ((i//100)%2)==0 and ((i//1000)%2)==0:
        print(i, end=',')