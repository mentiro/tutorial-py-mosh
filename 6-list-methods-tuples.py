##Exercise
#Find the largest number in a list
#
# list=[10,9,6,13,5,33,1,30]
# max=list[0]
# for i in list:
#     if i>max:
#         max=i
# print(max)



###2D Lists

# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
#
# print(matrix[1][0])
#
# for row in matrix:
#     for item in row:
#         print(item)



###List Methods (Functions)

# list=[5,2,4,7]
# list.append(10)
# list.insert(0,99)
# print(list)
# list.sort()
# print(list)
# list2=list.copy()
# print(list2)

##Exercies
#Remove the duplicates in a list

# list=[1,2,10,3,4,5,10,6,7,8,9,10]
# list_no_dup=[]
# for i in list:
#     if i not in list_no_dup:
#         list_no_dup.append(i)
# list_no_dup.sort()
# print(list_no_dup)


###Tuples
# list=(1,2,3)    #tuples use round paranthesis
#a Tuple cannot be changed - this is the main difference to lists


###Unpacking
coordinates=(1,2,3)
x,y,z=coordinates   #this will assign each variable to the values in the tuple
print(x)
