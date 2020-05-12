'''
Please write a binary search function which searches an item in a sorted list. 
The function should return the index of element to be searched in the list.
'''

def Ex67():
    print('start')
    num_list = [46,23,79,64,96,41,47,63,93,24]
    number = 24
    num_list.sort()

    low = 0
    high = 9
    
    mid = int((low + high)/2)

    while low != high:
        if number == num_list[mid]:
            return 'VALUE FOUND'
        elif number > num_list[mid]:
            low = mid
            mid = int((low + high)/2)
        elif number < num_list[mid]:
            high = mid
            mid = int((low + high)/2)
    return "NOT FOUND"

if __name__ == "__main__":
    print(Ex67())
    print('end')