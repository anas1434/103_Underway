'''
Please write assert statements to verify that every number in the list [2,4,6,8] is even.
'''

def Ex65():
    ls = [2,4,6,8]
    for num in ls:
        assert num%2 == 0

if __name__ == "__main__":
    Ex65()