'''
By using list comprehension, please write a program to print the list after 
removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
'''

def Ex81():
    raw_list = [12,24,35,70,88,120,155]
    return [x for x in raw_list if x%5!=0 or x%7!=0]

if __name__ == "__main__":
    print(Ex81())
