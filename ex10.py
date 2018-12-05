# tab with \t
tabby_cat = "\tI'm tabbed in."
# \n feeds a line 
persian_cat = "I'm split\non a line."
#  \\ creates a backslash
backslash_cat = "I'm \\ a \\ cat."

# using tab within """ quotes and the return carriage before Grass
# triple single quotes are stylistically different than """ but same effect
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
# using a format call with a quote...they get tricky coding in editors because extra " " show up....
print(f"\"Well isn't this just lovely,\" she said about the first letter of the sentence, who simply replied, \"{tabby_cat}.\"")