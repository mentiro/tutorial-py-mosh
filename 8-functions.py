# ###Functions
# def greet_user():       #defining a function
#     print("Hello sucker!")
#     print("Wussup?")
#
# greet_user()        #calling the function
#
# print()
#
#
# ##Pass a parameter/argument to the function
# def say_hello(name):        #name is the parameter
#     print(f'Wussup {name}')
#
# say_hello("Bibi")           #Bibi is the argument
# say_hello("Marioara")
#
# print()
#
# def say_hello_again(f_name, l_name):
#     print(f'Hi {f_name} {l_name}')
#
# #Positional arguments
# say_hello_again("Bibi", "Marioara")
# #Keyword arguments
# say_hello_again(l_name="Smithy", f_name="Johnny")
#
# print()
#
#
#
# ##Return statement
# def square(num):
#     return num*num      #By default, all functions return None - use return to return the value of the function
#
# print(square(3))



##Reusable function
#Reorganize the Emoji tutorial (02:26:21 in the course) to use Functions.

# message=input("> ")
# words=message.split(" ")
# emojis={
#     ":)":"Happy",
#     ":(":"Sad",
#     ":|":"Speechless",
#     ":/":"Unconvinced"
# }
# output=""
# for word in words:
#     output+=emojis.get(word, word)+" "
# print(output)

#Solution

def emoji_converter(message):
    words=message.split(" ")
    emojis={
        ":)":"Happy",
        ":(":"Sad",
        ":|":"Straightface",
        ":/":"Skeptical"
    }
    output=""
    for word in words:
        output+=emojis.get(word, word)+" "
        return output

message=input("> ")
print(emoji_converter(message))
