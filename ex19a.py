#  rpgs = rpg titles, hbc=hardback count, vgc = video game count
def rpg(hbc, vgc, name):
    print(f"I found {hbc} hardback rpgs on {name}'s bookshelf!")
    print(f"I found {vgc} video game RPGs on disc or steam at {name}'s house!")
    print(f"That's a lot of games!  I think {name} must be one of those gamer-geeks!\n")
# don't forget to dedent!

# direct code method
name1 = "Justin"
print(f"I went to {name1}'s house, and here is how many games I found:")
n1book = 125
n1vid = 231
rpg(n1book, n1vid, name1)

# we can use variables
name2 = "Chad"
print(f"{name2} emailed me variables to define his games:")
n2book = 2
n2vid = 5
rpg(n2book, n2vid, name2)
print("Actually, on second thought...that's pretty normal for a contractor.\n")

# adding math to predefined variables
name3 = "Will"
print(f"{name3} said he bought everything in {name2}'s collection, and then bought 10 more of each!: ")
n3book = n2book + 10
n3vid = n2vid + 10
rpg(n3book, n3vid, name3)

# Just doing math, no variables
print(f"I demand a recount for {name3}!  We found 200 more rpg books and 250 more videogame rpgs!!")
rn3book = n3book + 200
rn3vid = n3vid + 250
rpg(rn3book, rn3vid, name3)

# now it is YOUR TURN
yourname = input("Hey there!   What is your name? --> ")
youhb = input("Okay buddy, how many hardback rpg's do YOU HAVE? --> ")
youvid = input("and be honest... how many videogame rpg's do YOU HAVE? --> ")
print(f"WHOA!   Hey everybody, check this out!!!!   (points at {yourname}).")
rpg(youhb, youvid, yourname)

# don't forget to converst string into integer from input!
youhbint = int(youhb)
youvidint = int(youvid)
print(f"We have visisted the following people: {name1} {name2} {name3} and {yourname}.")
btot = n1book + n2book + rn3book + youhbint
vtot = n1vid + n2vid + rn3vid + youvidint
print(f"We found a total of {btot} hardback books and {vtot} RPB video game titles." )
print("What about duplicate titles among them?!  Ummm it's not like they share!")
print("GREEEEEDY NERDSESES")

