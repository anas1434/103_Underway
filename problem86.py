'''
By using list comprehension, 
please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].
'''

def Ex86():
    raw_list = [12,24,35,24,88,120,155]
    return [x for x in raw_list if x!=24]

if __name__ == "__main__":
    print(Ex86())
