# Let's create some variables

name = "Brad Lund"
age = 44 # not a lie
height = 70 # inches
weight = 215 # pounds
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# when printing, spacing DOES matter as we insert the variables using a f function
# the f stands for formatting and we are telling python to format the variable inside
# the line.
print(f"Hello, this is a little about me, {name}.")
print(f"I am {height} inches tall.")
print(f"I am {weight} pounds heavy.")
# Notice how I don't use an 'f' because we aren't using printing variables
print("I'm not that heavy although I could probably lose a few pounds.")
# need an f here, forward because we are formatting variables again
print(f"I have {eyes} eyes and {hair} hair.")
print(f"My teeth are always {teeth} because I don't drink coffee.")

# this line is tricky and make sure you get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

# let's convert the result in centimeters
cm_height = height * 2.54 # 2.54 cm in an inch
print(f"My height in centimeters is {cm_height}.")
# new total calculation for cm height
new_total = age + cm_height + weight
print(f"If I convert height to centimeters, the new total is {new_total}.")

# these two lines round up if you don't like the floats
# I tried to perform the round funciton inside but got an error, so I split out
# a variable for round_total
round_total = round(new_total)
print(f"If you don't like floating numbers, that value is rounded to {round_total}.")

# I figured it out...just put whole function inside curly brackets as if it is a 
# separate line of code.  It worked!

print(f"Testing does this total work?  Viz: {round(new_total)}.")


