from PIL import Image

im = Image.open('oxygen.png')

y = im.height/2
for x in range(0,im.width-20, 7):
	xy = (x, y)
	char = im.getpixel(xy)[0]
	print(chr(char), end = '')

print('')

#hard code, cause easier
array = [105, 110, 116, 101, 103, 114, 105, 116, 121]

#conversion
for n in range(0, len(array)):
	array[n] = chr(array[n])

key = ''.join(array)
print("key is %s" % key)
print("http://www.pythonchallenge.com/pc/def/%s.html" % key)