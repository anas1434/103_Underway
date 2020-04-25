'''
Define a function that can accept two strings as input and print the string with maximum length in console. 
If two strings have the same length, then the function should print all strings line by line.

'''

def Ex30():
    input1 = input("enter 1st input")
    input2 = input("enter 2nd input")
    if len(input1) == len(input2):
        return input1 + '\n' + input2
    return input1 + input2

if __name__ == "__main__":
    print(Ex30())