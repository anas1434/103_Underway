'''
Write a program which can map() to make a list whose elements 
are square of elements in [1,2,3,4,5,6,7,8,9,10].
'''

def Ex41(num):
    
    return num**2

if __name__ == "__main__":
    
    print(list(map(Ex41, [1,2,3,4,5,6,7,8,9,10])))
