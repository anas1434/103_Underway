'''
Please generate a random float where the value is between 10 and 100 using Python module.
'''
import random
def Ex68():
    y = random.randint(10,101)
    x = random.random()
    return x + y

if __name__ == "__main__":
    print(Ex68())