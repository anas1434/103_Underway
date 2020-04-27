'''
Define a function which can generate and print a tuple 
where the value are square of numbers between 1 and 20 (both included).
'''

def Ex37():
    return tuple(x**2 for x in range(1, 21))

if __name__ == "__main__":
    print(Ex37())