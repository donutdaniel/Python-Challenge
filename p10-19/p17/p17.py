import urllib.request
import re

#global variables
begin = 12345

#recursive web crawler function. O(n) time
def spider(curr):
	#request url, fetch html
	url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=%s" % curr
	with urllib.request.urlopen(url) as response:
		html = response.read().decode("utf-8")

	#see what the page tells us
	print(html)
	print()
	next = parse(html)

	#check if divide
	if re.search('Divide', html) != None:
		print("dividing...")
		next = int(curr)/2
	elif next == '': #if not divide, then must by key
		return html;

	#recursive call
	return spider(next)

#parses a "nothing is" string, returns the number
def parse(html):
	#check for false numbers
	temp = re.search('busynothing is \d+', html)
	if temp != None:
		html = temp.group(0)
	num = ''.join(re.findall('\d+', html))
	return num



key = spider(begin)
print("The key is %s" % key)
print("http://www.pythonchallenge.com/pc/def/%s" % key)
