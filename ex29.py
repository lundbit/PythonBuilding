# set your constants
people = 20
cats = 30
dogs = 15

# if statement tells code to do something based on operation
# indent four spaces just like a function because its a BLOCK of code
# dont forget to dedent
# if statement is a branch -- if true, run it, otherwise, skip
if people < cats:   # python expects indentation after colons
    print("Too many cats!  The world is dooooooomed!!")

if people > cats:
    print("Not many cats!  The world is saved! (sigh of relief)")

if people < dogs:
    print("The world is drooled on; too many dogs!!")

if people > dogs:
    print("The world is dry!")

# same as taking dogs (initially 15) and adding 5 (so now 20)
# 
dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.", dogs)



