'''
Python has many built-in functions, and if you do not know how to use it, 
you can read document online or find some books. But Python has a built-in document function 
for every built-in functions.

Please write a program to print some Python built-in functions documents, 
such as abs(), int(), raw_input()

And add document for your own function
'''


def Ex24():
    '''
    This is the documentation I created for problem 24.
    '''
    return 'Hello'

if __name__ == "__main__":
    print(abs.__doc__, '\n')
    print(int.__doc__, '\n')
    print(Ex24.__doc__)
