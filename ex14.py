from sys import argv

# script will come from the command lind in your shell
# user_name will come user input.
# There are two paramters total
script, user_name, gender = argv
# you can change your prompts with variables for variety
prompt = ':) --> '
prompt1 = ":| -->"
prompt2 = ":o -->"
# this line uses the two argumetns passed through the CL (user_name and gender)
print(f"Hi {user_name}, I'm the {script} script!  I can tell you are a {gender}.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt1)

print("What kind of computer do you have?")
computer = input (prompt2)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}.  Not sure where that is.
And you have a {computer} computer.  Nice.
""")