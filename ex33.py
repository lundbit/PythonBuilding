# i = 0
# numbers = []

# while i < 6:
#     print(f"At the top of i is {i}")
#     numbers.append(i)

#     i += 1
#     print("Numbers now: ", numbers)

#     print(f"At the bottom i is {i}")

# print("The numbers: ")

# for num in numbers:
#     print(num)


def fill(n, x, list):
    if n < x:
        print(f"At the top of i is {n}")
        list.append(n)

        n += 1
        print("Numbers now: ", list)
        print(f"At the bottom i is {n}")
        # don't forget to call function within the function to resemple a loop!   Better than while loops....
        fill(n, x, list)
    return list  # need this for when the value is null...return allows loop to end with last valid test #

x = int(input("Pick an integer ->"))

numbers = fill(0, x, [])
print("The numbers (remember 0 is a numbah too!  the first index): ")
for num in numbers:
    print(num)


