'''
Define a function which can compute the sum of two numbers.
'''

def Ex26(num1 = 0, num2 = 0):
    num1 = int(input('Enter 1st number: '))
    num2 = int(input('Enter 2st number: '))
    return num1 + num2

if __name__ == "__main__":
    print(Ex26())
