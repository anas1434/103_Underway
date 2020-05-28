'''
Please write a program which accepts a string from console and print the characters that have even indexes.

Example: If the following string is given as input to the program:

H1e2l3l4o5w6o7r8l9d

Then, the output of the program should be:

Helloworld
'''

def Ex92():
    raw_input = input()
    for char in raw_input:
        if raw_input.index(char)%2 == 0:
            print(char, end='')

if __name__ == "__main__":
    Ex92()