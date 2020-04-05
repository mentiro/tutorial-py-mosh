###Exceptions

# age=int(input("Age: "))
# print(age)

#When we run this code the process will:
# Return 0 = ended successfully
#If we type in a string instead of an int:
#Exit code 1 = program has crashed


try:
    zip_code=int(input("Your ZIP Code: "))
    str_number=int(input("Your House Number: "))
    result=zip_code/str_number
    print(zip_code)
except ValueError:      #what should happen if the program encounters an error of type ValueError
    print("Invalid value")
except ZeroDivisionError:
    print("House number cannot be 0")   #what should happen if the program encounters an error of type ZeroDivisionError

#Left at: 03:02:00 - Classes
