'''
With a given tuple (1,2,3,4,5,6,7,8,9,10), 
write a program to print the first half values in one line and the last half values in one line.
'''

def Ex38():
    tu = (1,2,3,4,5,6,7,8,9,10)
    for num in tu:
        if tu.index(num) < len(tu)/2:
            print(num, end=',')
    print("")
    for num in tu:
        if tu.index(num) >= len(tu)/2:
            print(num, end=',')

if __name__ == "__main__":
    Ex38()