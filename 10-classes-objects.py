###Classes
# class Point:
#     def move(self):   #This is a Method within a Class
#         print("move")
#     def draw(self):
#         print("draw")
#
# #an Object is an instance of a Class
# point1=Point()
# point1.draw()

#Constructors
# class Point2:
#     def __init__(self, x, y):
#         self.x=x
#         self.y=y
#     def move(self):
#         print("move")
#     def draw(self):
#         print("draw")
#
# point2=Point2(5, 10)
# point2.x=7
# print(point2.x)


#Exercise
#Define a new type called "Person"
#should have a "name" attribute and a "talk()" method

# class Person:
#     def __init__(self, name):
#         self.name=name
#     def talk(self):
#         print(f"Hi, I'm {self.name}")
#
# john=Person("Johnny B")
# john.talk()
#
# mary=Person("Mary J")
# mary.talk()


#Self practice - a class for an Employee
class Employee:
    def __init__(self, fname, lname, department, company, senior):
        self.fname=fname    #this can be written as self.first=fname - it is good to keep them the same though
        self.lname=lname
        self.department=department
        self.company=company
        self.email=fname+"."+lname+"@"+department+"."+company+".com"
        self.senior=senior
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)    #using self so that the Method works with all of the instances of the Class

emp_1=Employee("James", "Dean", "Movies", "Warner Bros", True)
emp_2=Employee("John", "Bongiovi", "Music", "Cat Music", True)
emp_3=Employee("Groot", "Grooty", "Botanical", "Home", False)
emp_4=Employee("Mizse", "Octopus", "H2O", "Home", False)

print(emp_3.department)
print(emp_1.senior)
#Ways to display the same result
print(emp_1.fullname())
print(Employee.fullname(emp_1))




#Left at Inheritance - 3:14:55
