'''
Define a function which can generate and print a list where 
the values are square of numbers between 1 and 20 (both included).
'''

def Ex33():
    return [x**2 for x in range(1, 20)]

if __name__ == "__main__":
    print(Ex33())