favFoods = ["Pizza", "Ice Cream", "Noodles"]
print(favFoods[0])  # index starts at 0
print(favFoods[2])
print(favFoods)

favFoods.append("Yogurt")  # adds stuff to end of the list
print(favFoods)
print("My 4th favorite food is " + favFoods[3])

favFoods.insert(1, "Chicken")  # adds to list but you can choose its index
print(favFoods)

favFoods.remove("Chicken")  # removes from list by name 
print(favFoods)

favFoods.pop(0) # removes by index
print(favFoods)

favFoods.insert(0, "Pizza") 

for food in favFoods:  # loops through a list
	print(food)


# My turn: loop through the list and add all the numbers together and then print the sum
numList = [0,1,2,3,4,5,6,7]
sum = 0
for num in numList:
	sum = sum + num
print(sum)

print(len(favFoods))  # function to get the length of the list

# My turn: make a list for favorite movies
# prompt for a favorite movie

# Example
myFood = input("What is your favorite food? ")
favFoods.append(myFood)
print(favFoods)

# my turn
favMovies = ["Shrek", "Shrek 2", "Shrek 3", "Shrek 4"]
myMovie = input("What is your favorite movie? ")
favMovies.append(myMovie)
print(favMovies)


# list of methods
# append - adds an item to the end of a list
# insert - adds an item to a specified index 
# remove - removes a specified item from a list
# pop - removes an item from a specified index

# list of functions
# len - returns the length of a list

print(favFoods[len(favFoods)-1])  # prints the last part of the list