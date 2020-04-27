'''
Write a program which accepts a string as input to print 
"Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".
'''

def Ex40():
    raw_input = input()
    if raw_input == "yes" or "YES" or "Yes":
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    Ex40()