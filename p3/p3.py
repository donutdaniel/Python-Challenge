import string
import sys

#error output if no data file provided
if len(sys.argv) < 2:
	print("Error. Please provide input file.")
	sys.exit()

#reads file containing string to be analyzed
#converts to string called data
data = open(sys.argv[1], 'r').read().replace('\n', '')

#global variable
key = ""
array = []

#Function that takes in a string of size 9, and analyzes for correct format
def bodyguard(s):
	if s[0].islower() and s[1:4].isupper() and s[4].islower() and s[5:8].isupper() and s[8].islower():
		array.append(s[1:8])

#loop through each 9 letter combo, find bodyguards
for i in range(0, len(data)-8):
	bodyguard(data[i:i+9])

#concatenate all small letters
for word in array:
	key += word[3]

print("Array of possible 'bodyguard' strings: %s" % array)
print()
print("All small numbers stitched together: %s" % key)
print("The key is %s" % key)
print()
print("http://www.pythonchallenge.com/pc/def/%s.html" % key)
print("Real link is .php: http://www.pythonchallenge.com/pc/def/%s.php" % key)