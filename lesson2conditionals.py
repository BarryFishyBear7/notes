# conditionals

age = input("What is your age? ") # prompt for age

# check if the age is more than 17, so the person can see R rated movies 

age = int(age) # change age into a number so we can compare it to 17
if age > 17: # everything in the if statement only runs if the statement is true
	print("You can see an R rated movie")

else:
	print("You cannot see an R rated movie, too bad")

print("Have a nice day!")
# you can check all these conditions
# >, <, > =, <=, == (== means equal to)

birthday = input("Is today your bithday? ")
 
if birthday == "yes": # case sensitive, Yes wouldn't work
	print("Happy Birthday!")

print("Have a nice day!")

myNum = 7
guess = input("Guess a number between 1 and 10")
guess = int(guess)

if guess == myNum:
	print("You guessed correctly! ")

elif guess > myNum: # another if statement (else if)
	print("Too high! ")

else:
	print("Too low! ")