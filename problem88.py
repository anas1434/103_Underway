'''
With a given list [12,24,35,24,88,120,155,88,120,155], 
write a program to print this list after removing all duplicate values with original order reserved.
'''

def Ex88():
    raw_list = [12,24,35,24,88,120,155,88,120,155]
    return list(set(raw_list))

if __name__ == "__main__":
    print(Ex88())
