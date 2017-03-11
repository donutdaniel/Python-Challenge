import re

def spider(next):
	file = open('channel/' + next + '.txt', 'r');
	data = file.read()
	#dispay data
	print(data)
	#parse, then go onto next
	nothing = parser(data)
	if nothing != '':
		spider(nothing)

#parses a "nothing is" string (taken from p4)
def parser(data):
	#check for false nums
	temp = re.search('the next nothing is \d+', data)
	if temp != None:
		data = temp.group(0)
	return ''.join(re.findall('\d+', num));