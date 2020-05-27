'''
Define a class Person and its two child classes: Male and Female. All classes have a method 
"getGender" which can print "Male" for Male class and "Female" for Female class.
'''

class Person():
    def get_gender(self):
        return 'unknown'

class Male(Person):
    def get_gender(self):
        return 'Male'
        
class Female(Person):
    def get_gender(self):
        return 'Female'

if __name__ == "__main__":
    Alex = Male()
    print(Alex.get_gender())
    Sara = Female()
    print(Sara.get_gender())
