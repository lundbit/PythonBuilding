#  assigning valuables to variables re: a commute calculator
#  notice how some variables can be assigned numbers, or previously 
#  established variables
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
avg_passengers_per_car = passengers / cars_not_driven

#  Here is the output using the variables, notice how you don't need to nest spaces
#  around the variables
#  Debug note:  Makes sure all intended text goes into quotations!
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", avg_passengers_per_car, "in each car.")
