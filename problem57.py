'''
Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.
'''

def Ex57():
    s = input()
    u = s.encode('utf-8')
    print(u)

if __name__ == "__main__":
    Ex57()