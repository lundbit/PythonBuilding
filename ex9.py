# Here's some new strange stuff, remember type it exactly.

# variable days is a string of days of the week
days = "Mon Tue Wed Thurs Fri Sat Sun"

# This is also a string, bu with line breaks using the new line argument \n
# BREAK:  add tons of space after a month --> actually not broken, just ugly
# BREAK:  remove n before Aug --->  "Jul\Aug"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# BREAK: forget the comma see what happens --> invalid syntax
print("Here are the days: ", days)
print("Here are the months: ", months)

#  triple quotes allows open text entry and editing
#  BREAK:  misuse the quotes...get it?   Don't put spaces between triple quotes
print("""
There's something going on here.
With the three double quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")
