'''
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its 
input and then check whether they are divisible by 5 or not. The numbers that are divisible 
by 5 are to be printed in a comma separated sequence.

Example:

0100,0011,1010,1001

Then the output should be:

1010
'''
def binaryToDecimal(binary): 
      
    
    decimal, i = 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return decimal

def Ex11():
    binary_list = input().split(',')
    
    for num in binary_list:
        a = int(num)
        if (binaryToDecimal(a))%5 == 0:
            print(num) 
    return 'end'


if __name__ == "__main__":
    Ex11()