'''
Write a program which can map() and filter() 
to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
'''

def Ex42(num):
    if num % 2 == 0:
        return num**2
    else:
        return False

if __name__ == "__main__":
    print(list(filter(Ex42, [1,2,3,4,5,6,7,8,9,10])))