def add(a,b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a,b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a,b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a,b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!!")


age = add(40, 5)
height = subtract(76, 4)
weight = multiply(100, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height {height}, Weight {weight}, IQ {iq}")

# A puzzle for extra credit, typing it in anyway
print("Here is the puzzle:")
# working 'backwards' per math rules... 25...220 --> multiply(200, 25) --> 5000
# next operation is subtract (72, 5000)
# becomes add(45, [72-5000])
# becomes 45 + -4928 --> -4883

# this recycles the above functions in a cool way
what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print("That becomes: ", what, " Can you do it by hand?")


