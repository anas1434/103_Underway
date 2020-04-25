'''
Define a function which can print a dictionary where the keys are numbers between 1 and 20 
(both included) and the values are square of keys.
'''

def Ex31():
    dictionary = {}
    for num in range(1, 21):
        dictionary.update({num : num**2})
    return dictionary

if __name__ == '__main__':
    print(Ex31())