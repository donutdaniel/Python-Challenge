from PIL import Image, ImageDraw
import math

def separate(img):
	newsize = (math.floor(img.width/2), math.floor(img.height/2))
	#evens
	even = Image.new('RGB', newsize, 'black')
	#odds
	odd = Image.new('RGB', newsize, 'black')
	evend = ImageDraw.Draw(even)
	oddd = ImageDraw.Draw(odd)

	for x in range(0, img.width):
		for y in range(0, img.height):
			xy = (math.floor(x/2), math.floor(y/2))
			if (x+y)%2 == 0:
				evend.point(xy, img.getpixel((x,y)))
			else:
				oddd.point(xy, img.getpixel((x,y)))
	even.save('even.jpg')
	odd.save('odd.jpg')

img = Image.open('cave.jpg')
separate(img)

print("key is evil")