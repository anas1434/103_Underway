'''
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

Suppose the following input is supplied to the program:

        Hello world
        Practice makes perfect

Then, the output should be:

        HELLO WORLD
        PRACTICE MAKES PERFECT
'''

def Ex9():
    string_list = []
    string = '@'
    while string !='':
        string = input()
        string_list.append(string)
    string_list = [char.upper() for char in string_list]
    return '\n'.join(string_list)

if __name__ == "__main__":
    print(Ex9())
