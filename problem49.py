'''
Define a class named Shape and its subclass Square. 
The Square class has an init function which takes a length as argument. 
Both classes have a area function which can print the area of the shape 
where Shape's area is 0 by default.
'''

class Shape():

    @staticmethod
    def area():
        '''
        this is a docstring
        '''
        print("area is 0")

class Square(Shape):

    def __init__(self, side = 0):
        self.side = side

    def area(self):
        print(self.side**2)

if __name__ == "__main__":
    sqr = Square(4)
    sqr.area()