'''
Please write a program which count and print the 
numbers of each character in a string input by console.

Example: If the following string is given as input to the program:

abcdefgabc

Then, the output of the program should be:

a,2
c,2
b,2
e,1
d,1
g,1
f,1

'''

def Ex90():
    raw_input = input()
    raw_dict = {}
    for char in raw_input:
        if char in raw_dict.keys():
            raw_dict[char] += 1
        else:
            raw_dict[char] = 1
    for char in raw_dict.keys():
        print(char, ',', raw_dict[char])
            
    

if __name__ == "__main__":
    Ex90()