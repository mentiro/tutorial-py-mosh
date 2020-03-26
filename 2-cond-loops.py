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

price = 1000000
good_credit = False

if good_credit:
    downpayment = price*0.1
else:
    downpayment = price*0.2
print("You will need to put down $" + str('%.0f' % downpayment))    #"'%.0f' % downpayment" - 0 decimal points
print(f"You will need to put down ${'%.0f' % downpayment}")         #same, but with formatted string


### Left at - 01:06:38 (Logical Operators) ###

###Logical Operators
