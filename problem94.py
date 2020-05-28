'''
Write a program to solve a classic ancient Chinese puzzle: We count 35 heads 
and 94 legs among the chickens and rabbits in a farm. 
How many rabbits and how many chickens do we have?
'''

def Ex94():
    #initial count
    count_dict = {'rabbit':0, 'chicken':0}

    #Define a condition to count legs
    def condition(count_dict):
        total_legs = (count_dict['rabbit'] * 4) + (count_dict['chicken'] * 2)
        return total_legs == 94

    while True:
        count_dict['rabbit'] += 1
        count_dict['chicken'] = 35 - count_dict['rabbit']
        if condition(count_dict):
            print('There are ',count_dict['rabbit'] ,'Rabbits')
            print('There are ',count_dict['chicken'], 'Chickens')
            return

if __name__ == "__main__":
    Ex94()
