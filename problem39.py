'''
Write a program to generate and print another tuple 
whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
'''

def Ex39():
    tu = (1,2,3,4,5,6,7,8,9,10)
    
    return tuple([x for x in tu if x%2==0])

if __name__ == "__main__":
    print(Ex39())