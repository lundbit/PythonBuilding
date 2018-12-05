# to run this in python you need to type: "python ex13.py arg arg arg" in the command shell
# 'arg' is an argument - you can type"pig dog sheep" or "first 2nd 3rd"...etc
# you must enter three parameters to match the three arguments expected by argv to avoid error

from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
food = input("What is your favorite food?")
print(f"I see that your favorite food is {food}.   Me too!!")

