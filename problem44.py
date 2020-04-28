'''
Write a program which can map() to make a list whose elements 
are square of numbers between 1 and 20 (both included).
'''

def Ex44():
    print(list(map(lambda x: x**2, list(range(1, 21)))))

if __name__ == "__main__":
    Ex44()