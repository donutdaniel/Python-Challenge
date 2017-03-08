import string
import sys

#error output if no data file provided
if len(sys.argv) < 2:
	print("Error. Please provide input file.")
	sys.exit()

#reads file containing string to be analyzed
#converts to string called data
# ifile = sys.argv[1];
# with open(ifile, 'r') as myfile:
# 	data = myfile.read().replace('\n', '')

data = open(sys.argv[1], 'r').read().replace('\n', '')

#remove punctuation
#python3
table = data.maketrans('', '', string.punctuation)
key = data.translate(table)

#python2.7 implementation
#key = data.translate(None, string.punctuation)

print("key is %s" % key)
print("http://www.pythonchallenge.com/pc/def/%s.html" % key)