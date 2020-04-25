'''
Define a class, which have a class parameter and have a same instance parameter.
'''

class Person():
    person = 'Human'

    def __init__(self, name = 'name', age = 'age'):
        self.name = name
        self.age = age
    def print_info(self):
        print(f"{self.name} is {self.age} years old.")

def Ex25():
    John = Person('John', 20)
    John.print_info()

if __name__ == "__main__":
    Ex25()
