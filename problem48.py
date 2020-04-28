'''
Define a class named Rectangle which can be constructed by a length and width. 
The Rectangle class has a method which can compute the area.
'''

class Rectangle():

    def __init__(self, length = 0, width = 0):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

if __name__ == "__main__":

    rect = Rectangle(10, 5)
    print(rect.get_area())
