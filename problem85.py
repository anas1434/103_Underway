'''
By using list comprehension, please write a program to print the list 
after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
'''

def Ex85():
    raw_list = [12,24,35,70,88,120,155]
    return [x for x in raw_list if raw_list.index(x)!=0 or raw_list.index(x)!=4 or raw_list.index(x)!=6]

if __name__ == "__main__":
    print(Ex85())
