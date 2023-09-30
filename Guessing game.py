# the guessing game
# write a program that generates a random number between 1 and 10
# lets the user guess what number was generated
# the result should be sent back to the user via a print statment
# import random 

from random import Random #importohet klasa

random_instance=Random()
random_number=random_instance.randint(0,10)


#user input
user_number=input("Put a random number 0 and 10 >> ")

#check if user input is number and between 0,10

if user_number. isdigit():

    if int(user_number)== random_number:
        print("you have guess right")
    else:
        print("you have guess wrong")
else:
    print("you did not put a number.")
