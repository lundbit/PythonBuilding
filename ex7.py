# BREAK:
print("Mary had a little lamb.")
# you can append the function call to the string that contains a {} call
# BREAK:
print("Its fleece was white as {}.".format('snow'))
# BREAK:
print("And everywhere that Mary went.")
# BREAK:
print("." * 10) # what'd that do?  It printed the period ten times

# BREAK: assign a string to end and add 'end' to print call --> very interesting
#        the string shows up like a normal string and the end=' ' does not overwrite
#        the end='byenumber' and still works to connect the lines Ceese and Burger
#        something static about end = " " AHA its a parameter built into the function

#end = "byenumber" #don't forget to add end as a variable below and see what happens

# BREAK:  remove a quote ->  EOL while scanning string literal
#end1 = C"

# BREAK:  mix single vs double quotes -> EOL while scanning string literal
# end1 = 'C"

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.  try removing it to see what happens
# as you found it it creates a syntax error

# BREAK: remove end=' ' -->  Cheese an Burger on separate lines
# print(end1 + end2 + end3 + end4 + end5 + end6)

# BREAK replace end with dog -->  dog is invalid keyword argument for print()
# print(end1 + end2 + end3 + end4 + end5 + end6, dog=' ')

# BREAK replace end=' ' with end = '@' -->  Cheese@Burger - another paramter!
# print(end1 + end2 + end3 + end4 + end5 + end6, end='@')

print(end1 + end2 + end3 + end4 + end5 + end6, end=' ') # declaring space variable end

# BREAK: put quotes around end7 variable -->  "Cheese end7urger"
# print("end7" + end8 + end9 + end10 + end11 + end12)

print(end7 + end8 + end9 + end10 + end11 + end12)