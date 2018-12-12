the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through elements in a list

# just pick a counter name, any counter name --> 'number' works
# remember the list you made called 'the_count'?
for number in the_count:
    print(f"This element is inside the list called 'the_count', in order, line by line: {number}")

# same as above
for fruit in fruits:
    print(f"This element is inside the list called 'fruit', in order, line by line: {fruit}")

# also we can go through mixed lists, too
# notice we have to use {} because we don't know what is in it
#  okay with using good old fashioned 'i' for your counter?
for i in change:
    print(f"I got {i}")

# we can also build lists, and with Python 3 can interate in a single line
elements = list(range(6))

# print the list iteration
print(f"It's magic!  We iterated these elements in the list!:", elements)

# METHODS
# .append() adds a number to the end of the list
# .insert(i, x)  insert x into index position i
# .extend(L)   insert L and exend the list you are applying method to do with new list
# .remove()   removes THE FIRST INSTANCE of the item from list --check your spelling--
# .pop([i])   returns what is populated at that index position
# .index('x')   returns where in the list x is FIRST positioned
# .copy()    copies the lists to become equivalent and usable for later manipulation
# .reverse()   reverses the items in a list
# .count('x')  counts how many times x occurs in the list
# .sort()   sorts in ascending order for integers and alphabetical for strings
# .clear() clears out the list

