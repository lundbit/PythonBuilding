# the use of single or double quotes tells python you want strings
# this program will introduce more strings and texts

# assign a number to a variable
types_of_people = 10
# assign a formatted string to a variable, x
x = f"There are {types_of_people} types of people."
binary = "binary" # assign a string to a variable
do_not = "don't" # another string to a variable
# the result is a string within a string!
y = f"Those who know {binary}, and those who {do_not}."

print(x)
print(y)

# string inside a string!
print(f"I said: {x}")
print(f"I also said: '{y}'")

# notice the boolean value is capitalized and that its a relief not to
# end each line in a semicolon...
hilarious = False
# assigning a FUNCTION within the string variable
joke_evaluation = "Isn't that joke so funny?! {}"

# sending the boolean value of hilarious 'through' the joke_evaluation variable
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."


# you can combine strings with additon because they are the same type
print(w + e)

# Breaking the code
#===================
# remove the comments to break using the following:

# f = 6
# print (w + e + f)

# you will see that you can't concatenate a str with an 'int'eger

# do you need a return carriage between lines?   Try this:
# print(f"I said: {x}")print(f"I also said: '{y}'")

# a separate line is required, which is good to know for linting options down the line

