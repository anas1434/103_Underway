'''
Define a custom exception class which takes a string message as attribute.
'''

def CustomException(Exception):
    def __init__(self, message):
        self.message = message
        return self.message

try:
    num = int(input())
except:
    raise CustomException("something is wrong")
