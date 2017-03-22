#recursive function for getting number at index, provided a first number
def lookSay(index, prev):
	if index == 0:
		return prev
	nextnum = ''
	sumnum = 0
	last = str(prev)[0]
	for x in str(prev):
		if x == last:
			#counting how many
			sumnum += 1
		else:
			#know how many (sumnum), then say
			nextnum += str(sumnum) + last
			sumnum = 1
		last = x
	#add the last one
	nextnum += str(sumnum) + last
	#recursive call
	print(nextnum)
	return lookSay(index-1, int(nextnum))


print("starting call of size 30...")
print("initial: 1")
num = len(str(lookSay(30, 1)))
print("len of index 30 is %i" % num)
print("key is %i" % num)
