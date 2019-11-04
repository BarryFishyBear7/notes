import time
import os

tenths = 0
seconds = 0
minutes = 0
hours = 0

while True:
	print(str(hours) + ":" + str(minutes) + ":" + str(seconds) + ":" + str(tenths))
	tenths = tenths + 1
	if tenths == 10:
		tenths = 0
		seconds = seconds + 1
	if seconds == 60:
		seconds = 0
		minutes = minutes + 1
	if minutes == 60:
		minutes = 0
		hours = hours + 1
	time.sleep(1/10)
	os.system("cls")