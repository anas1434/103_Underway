'''
Please write a binary search function which searches an item in a sorted list. 
The function should return the index of element to be searched in the list.
'''

def Ex67():
    num_list = [46,23,79,64,96,41,47,63,93,24]
    number = 47
    num_list.sort()
    x = int((low+high)/2)
    low = num_list[0]
    mid = num_list[x]
    high = num_list[9]
    

    while low != high:
        if number == mid:
            return 'VALUE FOUND'
        elif number > mid:
            low = mid
            mid = num_list[x]
        elif number < mid:
            high = mid
            mid = num_list[x]
    return "NOT FOUND"

if __name__ == "__main__":
    print(Ex67())