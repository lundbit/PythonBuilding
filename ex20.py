from sys import argv
script, input_file = argv

# f stands for file variable today
def print_all(f):
    print(f.read())

#goes to first BYTE in file
def rewind(f):
    f.seek(0)

def close(f):
    f.close()

def print_a_line(line_count, f):
    print(line_count, f.readline()) #readline seeking \ns to keep track of which line #

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like an old school cassette tape.")

rewind(current_file)

print("Let us print three lines!")

# we could have used any variable for current_line, and even assigned letters with right syntax
current_line = 1
print_a_line(current_line, current_file)

# line_count becomes what we tell it is...there is no real counting going on behind scenes
# increment with contractions!  :p
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

# not in Zed's original code but seems like a ok idea to me!
close(current_file)


