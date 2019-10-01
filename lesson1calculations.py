# Calculations, printing, variables

# Printing to the screen
# The built in function print() prints to the screen
# It will print both Strings and numbers

print("Printing to the screen...")
print("hello") # a string = inside quotes
print('hello again') # double and single quote marks work

print(6)  # print numbers
print("22") # a string again"
print(6+6) # you get 12
print ("6" + "6") # you get 66; adding this is called string concatenation
#print("6" + 6) ---- you get an error 

# Performing Calculations
# addition +
# subtraction - 
# multiplication *
# division /
# exponents **
# modulo %

print(4-2) # subtraction - 2
print(4*2) # multiplication - 8
print(4/3) # division - 1.33...
print(4**3) # exponents - 64

print("Modulo operator test")
print(5 % 3)
print(10 % 2)
print(16 % 3)
# Modulo gives remainders
# Python operators follow the same order of operations as Math
print(4-2*2) # should give 0
print((4-2)*2) # should give 4

# Variables
# variables are used to hold data
# variables are declared and set to a value --- setting the value is called initializing
badLuck = 13 # declared a variable called badLuck and intialized it to 13
# i can print the variable using it's name
print("badLuck = " + str(badLuck)) # cast it to a string
# let's do another one
goodLuck = "4" # String variable
print("goodLuck = " + goodLuck) # don't have to cast it because it's already a string
badLuck + 5 # this is pointless, doesn't change variable
print(badLuck) 
badLuck = badLuck + 5 # this does change variable, now badLuck = 18
print(badLuck)

# you can also save input into variables using input()
# a prompt goes inside the ()
name = input("what is your name?")
print("Hello " + name)
print(name*10)
name = name + "\n" # escape character (newline)
print(name * 10)

# let's try some math
base = input("Enter the base number: ")
exp = input("Enter the exponent: ")
print(int(base)**int(exp)) # you can also cast into integers