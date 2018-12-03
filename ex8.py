# formatter is a variable with a series of 4 arguments, {} {} {} {}
formatter = "{} {} {} {}"

# .format (a, a1, a2, a3) <<-- this is a FUNCTION called .format
# replace the 1, a1, with SIMILAR type variables (int, str, bool, variables)
# BREAK:  mix your types, or neglext to assign a 4 argument function to formatter
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print (formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
