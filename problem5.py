'''
    Define a class which has at least two methods:

        getString: to get a string from console input
        printString: to print the string in upper case.

    Also please include simple test function to test the class methods.

'''


class String():
    '''
        getString: to get a string from console input
        printString: to print the string in upper case.
    '''
    def __init__(*args, **kwargs):
        string = 'NO STRINGS ATTACHED'
    def getString(self):
        self.string = input("ENTER YOUR STATEMENT\n")
    def printString(self):
        print(self.string.upper())

if __name__ == "__main__":


    test = String()
    test.getString()
    print('')
    test.printString()