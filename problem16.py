'''
Use a list comprehension to square each odd number in a list. 
The list is input by a sequence of comma-separated numbers. 
Suppose the following input is supplied to the program:

1,2,3,4,5,6,7,8,9

Then, the output should be:

1,9,25,49,81
'''

def Ex16():
    result_list = []
    raw_input = input().split(',')
    for num in raw_input:
        if int(num)%2 !=0:
            result_list.append(str(int(num)**2))
    return ','.join(result_list)

if __name__ == "__main__":
    print(Ex16())