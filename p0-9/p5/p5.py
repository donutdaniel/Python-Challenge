import pickle

#load data
ifile = open('data.txt', 'rb')
obj = pickle.load(ifile)
ifile.close()

#load output file
ofile = open('out.txt', 'w');

#p is a list of lists of lists..I think ascii art!
#print to console and out.txt
#O(n^2)
for i in obj:
	for j in i:
		char = j[0]
		k = j[1]
		for x in range(0, k):
			print(char, end = '')
			print(char, end = '', file = ofile)
	#newline
	print('', end = '\n')
	print('', file = ofile)

ofile.close()