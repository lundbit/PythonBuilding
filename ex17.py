from sys import argv
# This returns a boolean if the file to be written to is going to be overwritten
from os.path import exists

# three calls this time.   Use echo > + cat in the CL to create and review first file
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
# assign the file to be opened first to a variable, then perform read function on variable
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

# if true...you are about to overwrite!  If false, you are essentially creating new
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, done.   I'll close both files now.")

# feel free to check your copy using the cat command on the CL

# make sure all your filenames and paths are correct!

out_file.close()
in_file.close()