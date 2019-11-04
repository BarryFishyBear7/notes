# How to tell if one number is a multiple of another

myNum = int(input("Enter a number to check: "))

print("Checking if your number is a multiple of 3 or 5...")

# hint: use % (gives you the remainder)
# check if the remainder is 0

if myNum % 3 == 0:
	print("Your number is a multiple of 3! ")

if myNum % 5 == 0:
	print("Your number is a multiple of 5! ")

else:
	print("Your number isn't a multiple of 3 or 5. ")



# how to print without a new line
print(str(myNum), end = "")
print(" something else")