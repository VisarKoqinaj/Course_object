# Write a program that takes your name as input
# and your agg as input
# and greats you with the following
# Hello <name>, on your next birthday you will be <age1>

name_input=input("Please give your name: ")
age_input=input("Please give your age: ")

if(len(name_input)>0 and len(age_input))>0:
    if age_input. isdigit():
        next_age=int(age_input) + 1
        print(f"Hello {name_input}, on your next birthday you will be {next_age}")

