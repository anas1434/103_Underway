'''
A robot moves in a plane starting from the original point (0,0). 
The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
The trace of robot movement is shown as the following:

UP 5
DOWN 3
LEFT 3
RIGHT 2

The numbers after the direction are steps. Please write a program to compute the distance from 
current position after a sequence of movement and original point. If the distance is a float, 
then just print the nearest integer. Example: If the following tuples are given as input to the program:

UP 5
DOWN 3
LEFT 3
RIGHT 2

Then, the output of the program should be:

2
'''
class Robot():

    def __init__(self, list_of_tuples=[]):
        self.list_of_tuples = []
        self.current_position = [0,0]
        while True:
            raw_input = (input("ENTER YOUR COMMANDS\n").split())
            if not len(raw_input) != 0:
                break
            self.list_of_tuples.append(tuple(raw_input))
            print(self.list_of_tuples)
    
    def move_robot(self):
        for command in self.list_of_tuples:
            if command[0] =='UP':
                self.current_position[1] += int(command[1])
            elif command[0] == 'DOWN':
                self.current_position[1] -= int(command[1])
            elif command[0] == 'RIGHT':
                self.current_position[0] += int(command[1])
            elif command[0] == 'LEFT':
                self.current_position[0] -= int(command[1])
    
    def robot_displacement(self):
        x1 = 0
        x2 = self.current_position[0]
        y1 = 0
        y2 = self.current_position[1]
        self.displacement = int((((x2-x1)**2) + ((y2-y1)**2))**(1/2))
        return self.displacement

if __name__ == '__main__':
    alex = Robot()
    alex.move_robot()
    print(alex.robot_displacement())
