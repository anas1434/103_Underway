'''
Please write a program to compress and 
decompress the string "hello world!hello world!hello world!hello world!"

Hints
Use zlib.compress() and zlib.decompress() to compress and decompress a string.
'''

import zlib

def Ex76():
    s = 'hello world!hello world!hello world!hello world!'
    #In Python 3 zlib.compress() accepts only DataType <bytes>
    y = bytes(s, 'utf-8')
    x = zlib.compress(y)
    print(x)
    print(zlib.decompress(x))

if __name__ == "__main__":
    Ex76()