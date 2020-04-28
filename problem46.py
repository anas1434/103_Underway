'''
Define a class named American and its subclass NewYorker.
'''

from problem45 import American

class NewYorker(American):
    @staticmethod
    def print_recidence():
        print("he is living in NYC")

if __name__ == "__main__":
    Alex = NewYorker()
    Alex.print_recidence()