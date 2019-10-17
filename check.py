# This is a check/review to make sure nothing was "lost" over fall break

# Brian Liu
# P1 10/14/19

# Variable declaration and assignment
# Example
myVar = "hello"
# My turn: declare two variables 1 string and 1 number
var1 = "string"
var2 = 34

# While loop
# Example
x = 10
while x > 0:
	print(x)
	x = x - 1
# My turn: print my name 100 times (don't use print("Brian" * 100))
y = 100
while y > 0:
	print("Brian")
	y = y - 1 

# String Concatenation
# Example
name = "Donze"
print("Hello " + name)
# My turn: make a variable with your favorite movie and print "my favorite movie is" ...
favoriteMovie = "Forrest Gump"
print("My favorite movie is " + favoriteMovie)

# Input 
# Example
yourName = input("What is your name: ")
print("Your name is " + yourName)
# My turn: prompt for favorite song and print "your favorite song is " ...
favoriteSong = input("What is your favorite song: ")
print("Your favorite song is " + favoriteSong)

# Casting - changing the type of a variable
myNum = 40
print("My number is " + str(myNum))
num1 = input("Enter a number: ")
num1 = int(num1) + 10
print("num1 + 10 is " + str(num1))

# My turn: ask for two numbers, add them and print
number1 = int(input("First number: "))
number2 = int(input("Second number: "))
sum = number1 + number2
print("The sum of your two numbers is " + str(sum))

# if/else 
# Example
num1 = int(input("Type a number: "))
if num1 > 100: 
	print("Your number is more than 100")
elif num1 == 100:
	print("Your number is equal to 100")
else:
	print("Your number is less than 100")

# My turn: Ask if today is your birthday, if it is print happy birthday
birthday = input("Is today your birthday? ")
if birthday = "Yes"
	print("Happy birthday!")
if birthday = "No"
	print("Too bad you  suck")