import re
import zipfile

begin = 90052
channelzip = zipfile.ZipFile('channel.zip', 'r')
comment = []

def readComments(next):
	com = channelzip.getinfo('%s.txt' % next).comment.decode("utf-8")
	comment.append(com)

def spider(next):
	file = open('channel/%s.txt' % next, 'r')
	data = file.read()
	#dispay data
	print(data)
	readComments(next)
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
	return ''.join(re.findall('\d+', data));

spider(begin)
print(''.join(comment))

