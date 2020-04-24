'''
Write a program that computes the net amount of a bank account based a transaction log from console input.
The transaction log format is shown as following:

D 100
W 200

D means deposit while W means withdrawal.

Suppose the following input is supplied to the program:

D 300
D 300
W 200
D 100
Then, the output should be:

500
'''

def Ex17():
    balance = 0
    input_list = []
    raw_input = '@'
    while raw_input != '':
        raw_input = input()
        input_list.append(raw_input)
    input_list.pop()
    for command in input_list:
        if command[0] == 'D':
            balance += int(command[2:])
        elif command[0] == 'W':
            balance -= int(command[2:])
        else:
            print("There is an invalid command")
    return balance

if __name__ == "__main__":
    print(Ex17())