people = input("How many people? ")
cars = input("How many cars? ")
trucks = input("How many trucks? ")

if cars > people: # cars take precedece over trucks and people
    print("We should take the cars.")
# elif is a second branch checkpoint and evaluates independently
elif cars < people:
    print("We should not take the cars.")
    # else is what happens if either branch operation doesn't hold true
else:   # implies people and cars are equal
    print("We can't decide.")

if trucks > cars: # don't prefer trucks over cars
    print("That's too many trucks.")
elif trucks < cars:  # if wayyy too many cars, then consider trucks
    print("Maybe we could take the trucks.")
else:   # implies cars and trucks are equal
    print("We still can't decide.")

if people > trucks:  # if too many people, use all avail trucks
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

