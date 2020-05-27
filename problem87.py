'''
With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], 
write a program to make a list whose elements are intersection of the above given lists.
'''

def Ex87():
    raw_set = set([12,24,35,24,88,120,155])
    raw_set1 = set([1,3,6,78,35,55])
    raw_set &= raw_set1
    return list(raw_set)

if __name__ == "__main__":
    print(Ex87())
