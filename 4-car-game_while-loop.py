###While Loop
# i=1
# while i<=10:
#     print(i)
#     i+=1
#
# j=1
# while j<=15:
#     print("|"*j)
#     j+=1
#
# print("End of the loops...awoooo!")


##Car Game
#There is a console where you can type 3 commands:
#start - starts the car
#stop - stops the car
#quit - exits the game
print("** Car Game instructions **")
print("Type in the following commands to play the game:")
print('''
start - starts the car
stop - stops the car
exit - quits the game
-comm - display this menu again
''')

commands=["start","stop","exit","-comm"]
car=True
car_start=False
while car:
    answer=input("> ").lower()
    if answer not in commands:
        print("Invalid command")
    elif answer=="start":
        if car_start==True:
            print("Car is already started")
        else:
            print("The car has started - ready to go!")
        car_start=True
    elif answer=="stop":
        if car_start==False:
            print("Car is already stopped")
        else:
            print("The car has been stopped")
        car_start=False
    elif answer=="-comm":
        print('''
        start - starts the car
        stop - stops the car
        exit - quits the game
        -comm - display this menu again
        ''')
    elif answer=="exit":
        print("Bye!")
        break
else:
    print("There is no car!")
