import string
import sys

if len(sys.argv) < 2:
	print("Error. Please provide input file.")
	sys.exit()

ifile = sys.argv[1];

with open(ifile, 'r') as myfile:
	data = myfile.read().replace('\n', '')

key = data.translate(None, string.punctuation)

print("key is %s" % key)

print("http://www.pythonchallenge.com/pc/def/%s.html" % key)