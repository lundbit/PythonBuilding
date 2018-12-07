# this one is like your scriptss with argv
# (def)ine function named 'print_two' and must use (*args) to work, end with a colon
# function names can't start with a number or have spaces, so use '_' and lowercase for style
def print_two(*args):
    #indent 4 spaces and unpack your arguments into 'args'
    arg1, arg2 = args   # <--- indent 4 spaces!  no more, no less
    print(f"arg1: {arg1}, arg2: {arg2}")
# dedent to signal the end of the function

# ok, that *args is actually pointless, we can just do this
# you can skip the (*args) and just assign the argument names in '(a,b):'
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2 {arg2}")

# this takes just one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothin'.")


print_two("Zed","Shaw")
print_two_again("Brad","Lund")
print_one("Whoa!")
print_none()