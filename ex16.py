from sys import argv

# call forth two arguments at the CL (the name of this script + the name of the text file
# that the program will write to)
script, filename = argv

#This allows you to extend the existing text file or erase it
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
# boom this actually wipe the file for a clean file which might obviate the truncate() below
target = open(filename, 'w')

# actually, 'w' wiped it.   Using "r+" instead, would make use of truncate()
print("Truncating the file.  Goodbye!  Muhahahaha")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file for you.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# can we combine them?   Remember one is a variable and the \n is a string....
# concatanate!
target.write(line1 + '\n' + line2 + '\n' + line3 + '\n')

print("Aaaand finally, we will close the file.")
target.close()

