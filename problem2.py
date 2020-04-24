'''
Write a program which can compute the factorial of a given
numbers.The results should be printed in a comma-separated 
sequence on a single line.Suppose the following input is 
supplied to the program: 8 Then, 
the output should be:40320
'''
def Ex2():

  from math import factorial

  x = int(input("ENTER A NUM: "))

  return factorial(x)

if __name__ == 'main':
    print(Ex2())
