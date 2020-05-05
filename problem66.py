'''
Please write a program which accepts basic mathematic expression from 
console and print the evaluation result.

Example: If the following n is given as input to the program:

35 + 3

Then, the output of the program should be:

38
'''

def Ex66():
    raw_input = input().split(' ')
    print(raw_input)
    num1 = (raw_input[0])
    num2 = raw_input[2]
    operator = (raw_input[1])
    if operator == '+':
        return int(num1) + int(num2)
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num2 * num1
    elif operator == '/':
        return num1 / num2

if __name__ == "__main__":
    print(Ex66())