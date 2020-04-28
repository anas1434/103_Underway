'''
Define a class named Circle which can be constructed by a radius. 
The Circle class has a method which can compute the area.
'''

class Circle():
    def __init__(self, radius = 0):
        self.radius = radius
    def get_area(self):
        return 3.14*(self.radius ** 2)

if __name__ == "__main__":
    circle = Circle(5)
    print(circle.get_area())