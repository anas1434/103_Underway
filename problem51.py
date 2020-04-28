'''
Write a function to compute 5/0 and use try/except to catch the exceptions.
'''

def Ex51():
    def divide():
        return 5/0

    try:
        divide()
    except:
        print("it is impossible")
    else:
        print("any other exceptions?")

if __name__ == "__main__":
    Ex51()