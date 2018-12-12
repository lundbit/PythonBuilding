def numbo(v):
    try:     i = int(v)
    except:  return False
    return True

print(""" You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    # nesting decisions
    if bear == "1":
        print("The bear eats your face off.  Good job!")
    elif bear == "2":
        print("The bear eats your legs off.  Good job!")
    else: # if they didn't type 1 or 2
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothspins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    elif numbo(insanity) == True: # this implies choosing 3 or higher #
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job.")
    else: # if they type text
        print("""The magic ward of your keyboard ports you into 
        H.P. Lovecraft's deli located in another dimension.
        Eat two sammies for free, close your eyes, count to three
        and then say the word 'Fanciful' while holding your tounge out
        six times while drumming fingers on your desk.
        
        You will then be home again.
        
        Don't do this again, idiot.
        
        The first room requires you to use the magic of your keyboard to
        survive the bear.   MUCH MUCH easier.""")
# lets use our function to determine if input is integer or not
# if numbo is true, then let them know they have wrong number
elif numbo(door) == True:
    print("You tricky hobbit....trying a different number!   You implode from your second breakfast!")

# if they simply typed jargon, this is the result
else:
    print("""You stumble around and fall on a knife and die.  Good job!
    
    You love being a smart ass don't you?   ONE or TWO...but noooo....
    Not you....""")

    print(isinstance(door, int))


