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
found = ""
array = []

#Function that takes in a string of size 9, and analyzes for correct format
def bodyguard(s):
	if s[0].islower() and s[1:4].isupper() and s[4].islower() and s[5:8].isupper() and s[8].islower():
		array.append(s[1:8])
		return s[1:8]

for i in range(0, len(data)-8):
	temp = bodyguard(data[i:i+9])
	if temp != None:
		found = temp


print(array)
print("The key is %s" % found)
print("http://www.pythonchallenge.com/pc/def/%s.html" % found)