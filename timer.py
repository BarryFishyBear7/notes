import time
import os

# variables
hours = 0
minutes = 0
seconds = 0

# input
print("Enter the number of hours, minutes, and seconds for the timer. ")
hours = int(input("Hours: "))
minutes = int(input("Minutes: "))
seconds = int(input("Seconds: "))

# convert everything into seconds
minutes += hours * 60
seconds += minutes * 60

# set hours and minutes to 0
minutes = 0
hours = 0

# start countdown loop
while seconds >= 0:
	# convert back to hours, minutes, and seconds to print time
	minutes = int(seconds / 60)
	seconds = seconds % 60

	hours = int(minutes / 60)
	minutes = minutes % 60

	# print time
	print(str(hours) + ":" + str(minutes) + ":" + str(seconds))

	# convert back to seconds so that we can subtract seconds
	minutes += hours * 60
	seconds += minutes * 60
	
	# set hours and minutes to 0
	minutes = 0
	hours = 0

	# pause for one second
	time.sleep(1)

	# clear screen
	os.system("cls")

	# subtract one second
	seconds = seconds - 1