# string
myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

# concatenation
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

# input
name = input("What is your name? ")
print(name)

# output
color = input("What is your favorite color? ")
animal = input("What is your favorite animal? ")
print("{}, you like a {} {}!".format(name,color,animal))
print(f"{name}, you like a {color} {animal}!")