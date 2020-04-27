'''
Define a function which can generate a list where the values are square of 
numbers between 1 and 20 (both included). Then the function needs to print 
the first 5 elements in the list.
'''

def Ex34():
    return [x**2 for x in range(1, 20)][:5]

if __name__ == "__main__":
    print(Ex34())