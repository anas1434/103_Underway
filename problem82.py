'''
By using list comprehension, please write a program to print the list after removing 
the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].
'''

def Ex82():
    raw_list = [12,24,35,70,88,120,155]
    return [x for x in raw_list if raw_list.index(x)%2==0]

if __name__ == "__main__":
    print(Ex82())
