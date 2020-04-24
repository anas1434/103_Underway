'''

    Write a program which accepts a sequence of comma-separated numbers 
    from console and generate a list and a tuple which contains every number.
    Suppose the following input is supplied to the program:
             34,67,55,33,12,98

Then, the output should be:
        ['34', '67', '55', '33', '12', '98']
        ('34', '67', '55', '33', '12', '98')


'''


def prog(string=""):

    global my_list
    string = input("ENTER NUMBERS: \n")
    my_list = string.split(',')
    my_tuple = tuple(my_list)
    return my_list


if __name__ == '__main__':
    my_list = []
    print(prog())
