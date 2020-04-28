'''
Assuming that we have some email addresses in the "username@companyname.com" format, 
please write program to print the user name of a given email address. 
Both user names and company names are composed of letters only.

Example: If the following email address is given as input to the program:

john@google.com

Then, the output of the program should be:

john

In case of input data being supplied to the question, it should be assumed to be a console input.
'''

class Info():

    def __init__(self,email = 'username@companyname.com'):
        self.email = input("enter your email")
    
    def get_name(self):
        a = self.email.index('@')
        print(self.email[:a])
    def get_company(self):
        a = self.email.index("@") + 1
        b = self.email.index(".")
        print(self.email[a:b])


if __name__ == "__main__":
    empl = Info()
    empl.get_name()