import datetime

validDates = []
for n in range(100):
	year = ""
	if n < 10:
		year = "10" + str(n) + "6"
	else:
		year = "1" + str(n) + "6"

	year = int(year)
	d = datetime.date(year, 1, 26)
	#check for 26th falling on a thursday
	if(d.weekday() == 0 and year%4 == 0):
		#check for leap year
		validDates.append(d)

print("Valid Years: " )
print(validDates)
print("Second from youngest is: ")
print(validDates[len(validDates)-2])
print("Mozart's birthday is tomorrow, on the 27th")