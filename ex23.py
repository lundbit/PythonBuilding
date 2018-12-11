import sys
script, encoding, error = sys.argv

# function main reads a line of code from language_file
def main(language_file, encoding, errors):
    line = language_file.readline()
     # output starting with 'b' is python telling you that raw bytes are being used

    # if a line can be read with readline() perform the function, otherwise, skip
    if line:
        # printing the line with a function print_line below
        print_line(line, encoding, errors) 
        # function main within main creates a loop that stops once if-statement fails
        return main(language_file, encoding, errors)

# encodes of each line from languages.txt
def print_line (line, encoding, errors):
    # strip removes the \n of the line string
    next_lang = line.strip()
    # encoding the language into raw bytes (Decode Bytes Encode Strings)
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # must use .decode() if working with raw bytes
    cooked_string = raw_bytes.decode(encoding, errors=errors)

# check to see what each looks like  -->  bytes to strings
    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding="utf-8")

main(languages, encoding, error)