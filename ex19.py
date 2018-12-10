#  cnc = chese and crackers, ccount=cheese count, boxofcrk = boxes of crackers
def cnc(ccount, boxofcrk):
    print(f"You have {ccount} cheeses!")
    print(f"You have {boxofcrk} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")
# don't forget to dedent!

# notice how 20, 30 don't match "ccount" and "boxofcrk"
print("We can just give the function numbers directly: (use 20 for cheese, 30 for crackers")
cnc(20,30)

# notice how aoc,aock don't match "ccount" and "boxofcrk"
print("OR we can use the variables from our script: (hardcode 10 and 50)")
#aoc = amount of cheese, aock = amount of crackers
aoc = 10
aock = 50
cnc(aoc, aock)

# notice how the math doesn't match "ccount" and "boxofcrk"
print("We can even do the math inside, too: (code says to add 10+20 for cheese and 5+6 for crackers)")
cnc(10 + 20, 5 + 6)

# notice how adding to later defined variables doesn't match "ccount" and "boxofcrk"
print("And we can combine the math and variables: (add 100 to amount of cheese/crackers")
cnc(aoc + 100, aock + 100)
