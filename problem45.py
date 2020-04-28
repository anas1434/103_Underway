'''
Define a class named American which has a 
static method called printNationality.
'''

class American():
    
    def printNationality(self):
        return 'American'

if __name__ == "__main__":
    David = American()
    print(David.printNationality())