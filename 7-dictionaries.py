###Dictionaries

# customer={      #we define a dictionary with curly braces
#     "name":"John Smith",
#     "age":30,
#     "is_verified":True
# }
#
# print(customer["name"])
#
# customer["birth_date"]="14-Jun-1987"    #append the birth_date to the customer dictionary
#
# print(customer["birth_date"])

##Exercise
#A program that asks for the phone number in digits and outputs it to words

phone_no=input("Enter your phone number: ")
converter={
    "0":"zero",
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
    "10":"ten"
}

word_list=""

for i in phone_no:
    word_list += converter.get(i)+" "
print(word_list)


##Left at 2:30:40 - Functions
