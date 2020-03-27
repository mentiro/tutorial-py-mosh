###If Statements
# one = False
# two = False
#
# if one:
#     print("This is One because it's " + str(one))
# elif two:
#     print("This is Two because it's " + str(two))
# else:
#     print("Neither One nor Two because they are both " + str(one))

#Exercise
# Price of a house is $1M
# If a buyer has good credit,
#   they neet to put down 10%
# Otherwise
#   they need to put down 20%
#Print the down payment

# price = 1000000
# good_credit = False
#
# if good_credit:
#     downpayment = price*0.1
# else:
#     downpayment = price*0.2
# print("You will need to put down $" + str('%.0f' % downpayment))    #"'%.0f' % downpayment" - 0 decimal points
# print(f"You will need to put down ${'%.0f' % downpayment}")         #same, but with formatted string


###Logical Operators
# x=True
# y=True
##and
# if x and y:
#     print("Both are True")
# else:
#     print("At least one is False")
##or
# if x or y:
#     print("At least one is True")
# else:
#     print("They must be both False")
##and not
# if x and not y:
#     print("x is True, y is False")
# else:
#     print("y is True")

###Comparison Operators
# a=10
# b=5
#
# a=str(a)
# b=str(b)
#
# if a>b:
#     print(a+" > "+b)
# elif a==b:
#     print(a+" = "+b)
# elif a!=b:
#     print(a+" != "+b)
# else:
#     print(a+" < "+b)

#Exercise
#if name < 3 characters
#   print name must be at least 3 characters
#else if name is more than 50 characters
#   print name can be max of 50 characters
#else
#   print that name looks good!

# name=input("What's your name? ")
# if len(name) < 3:
#     print("Your name must be at least 3 characters")
# elif len(name) > 50:
#     print("Your name must not exceed 50 characters")
# else:
#     print("Cool name!")
