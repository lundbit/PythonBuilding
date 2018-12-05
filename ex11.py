# end=' ' --> go to next line
# input() is a function that awaits an input from the user
# in this instance we are assigning the function to a variable
print("How old are you? (years)", end=' ')
age=input()
print("How tall are you? (ft/in)", end=' ')
height = input()
print("How much do you weigh?(lbs)", end=' ')
weight = input()

print(f"So, you're {age} years old, {height} tall and {weight} lbs heavy.")

print("Let's get a number from you...and please use numbers.")
yournum = input()
intcheck = int(yournum)
#would this work as easily? comment out the two lines before this and unhash the next line
#intcheck = int(input()) # converts string number into integer  (answer:  yes)
print(f"A-ha, here is your number {intcheck}.")