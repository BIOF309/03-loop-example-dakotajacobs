### --- Example of a simple loop --- ###

# First, step is to get user input of favorite numbers
favorite_number = input("Enter your favorite number: ")
second_favorite = input("Enter your second favorite number: ")
third_favorite  = input("Enter your third favorite number: ")
print (favorite_number, second_favorite, third_favorite)        # prints input
print ("Those are some good numbers")

# Second, convert user input to integers
favorite_integer = int(favorite_number)
second_integer = int(second_favorite)
third_integer = int(third_favorite)

# Third, make a list from the integers
list = []
list.append (favorite_integer)
list.append (second_integer)
list.append (third_integer)
print ("In a list they look like this")
print (list)                                                    # Checks list

# Lastly, provide a sum for each user input
print ("I'm going to tell you their sum, so buckle up")
sum = 0
for val in list:
    sum = sum+val
print (sum)
print ("Now you have a fourth favorite number")
