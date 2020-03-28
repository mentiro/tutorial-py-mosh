###For loops
# names=["Abi","Abu","Abba","Dabba"]
# for i in names:
#     print(i)
#
# for j in range(10):
#     print(j)
#
# #Print the sum of the elements of a list
# prices=[10,20,30,40,50]
# total=0
# for k in prices:
#     total+=k
# print(total)
#
#
# ###Nested loops
# for x in range(4):
#     for y in range(3):
#         print("("+str(x)+", "+str(y)+")")
#         print(f"({x}, {y})")    #same as above, but with formatted string

##Exercise
# Draw the figure F made of Xs with nested Loops:
# XXXXX
# XX
# XXXXX
# XX
# XX
# XX

list=[5,2,5,2,2,2]
for a in list:
    for b in range(a):
        print("X",end="")   # end-"" - print on the same line without spaces
    print("")

#Draw an L
print("\n")
list=[1,1,1,1,1,5]
for a in list:
    for b in range(a):
        print("X",end="")   # end-"" - print on the same line without spaces
    print("")

## Left at 1:56:00 - Lists
