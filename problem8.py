'''


    Write a program that accepts a comma separated sequence of words as input and prints 
    the words in a comma-separated sequence after sorting them alphabetically.

    Suppose the following input is supplied to the program:

                without,hello,bag,world

    Then, the output should be:

                bag,hello,without,world

'''
def Ex8():
    raw_input = input("enter the words \n ").split(',')

    raw_input.sort()
    for char in raw_input:
        print(char, end=',')

if __name__ == "__main__":
    Ex8()