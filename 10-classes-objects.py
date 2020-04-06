###Classes
# class Point:
#     def move(self):
#         print("move")
#     def draw(self):
#         print("draw")
#
# #an Object is an instance of a Class
# point1=Point()
# point1.draw()

#Constructors
class Point2:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def move(self):
        print("move")
    def draw(self):
        print("draw")

point2=Point2(5, 10)
point2.x=7
print(point2.x)


#Exercise
#Define a new type called "Person"
#should have a "name" attribute and a "talk()" method

class Person:
    def __init__(self, name):
        self.name=name
    def talk(self):
        print(f"Hi, I'm {self.name}")

john=Person("Johnny B")
john.talk()

mary=Person("Mary J")
mary.talk()

#Left at Inheritance - 3:14:55
