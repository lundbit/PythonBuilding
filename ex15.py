from sys import argv
# two parameters: name of .py program and filename to be read
script, filename = argv
# this variable will open the file assigned to filename
txt = open(filename)

print(f"Here is your file {filename}:")
# this is a read function upon the txt variable which contains filename
print(txt.read())

print("Type the filename again:")
# now instead of relying on the command line, or argv, the user inputs the filename
file_again = input("--> ")
# assigns user input to function open
txt_again = open(file_again)
# prints the result of the read function upon the UI inputted file instead of CL filename
print(txt_again.read())

# calling the filename by method through the command line avoids type errors that occur
# when using input() within the program.  You can control your flow and variables more
# through using methods to pass arguments.  

# ABC = Always Be Closing!   :p   <--- format is filename.closefunction()
txt.close()
txt_again.close()

