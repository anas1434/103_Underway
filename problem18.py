'''
A website requires the users to input username and password to register. 
Write a program to check the validity of password input by users.

Following are the criteria for checking the password:

At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12

Your program should accept a sequence of comma separated passwords and will check 
them according to the above criteria. Passwords that match the criteria are to be printed, 
each separated by a comma.

Example

If the following passwords are given as input to the program:

ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:

ABd1234@1
'''
import string

def Ex18():
    result = []
    raw_input = input().split(',')
    
    for pw in raw_input:
        lenght = 0
        a = False
        b = False
        c = False
        d = False
        for char in pw:
            if char in ['@','#','$']:
                lenght+=1
                a = True
            elif char in list(string.digits):
                lenght+=1
                b = True
            elif char in list(string.ascii_uppercase):
                lenght+=1
                c = True
            elif char in list(string.ascii_lowercase):
                lenght+=1
                d = True
            if len(pw) == lenght and lenght < 12 and lenght > 6 and a and b and c and d :
                result.append(pw)
    return ','.join(result)
            

if __name__ == "__main__":
    
    print(Ex18())