'''
Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].
'''

def Ex80():
    raw_list = [5,6,77,45,22,12,24]
    return [x for x in raw_list if x%2!=0]

if __name__ == "__main__":
    print(Ex80())
