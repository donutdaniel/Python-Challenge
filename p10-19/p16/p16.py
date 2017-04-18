from PIL import Image, ImageChops
import numpy as np

img = Image.open("mozart.gif")

colors = list(enumerate(img.histogram()))
#find pink, if appears once in every row
height = img.height
pink = 0
for x in colors:
	if x[1]%height == 0 and x[1] != 0:
		pink = x[0]

#align image
for y in range(height):
	#copy paste
	row = img.crop((0, y, img.width, y+1))
	#shift
	row = ImageChops.offset(row, -(row.tobytes().index(pink)))
	#insert back in
	img.paste(row, (0, y, img.width, y+1))

img.save("result.gif")
