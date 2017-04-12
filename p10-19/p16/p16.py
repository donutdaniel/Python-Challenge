from PIL import Image, ImageDraw
import numpy as np

img = Image.open("mozart.gif")

colors = list(enumerate(img.histogram()))
#find pink, if appears once in every row
height = img.height
pink = 0
for x in colors:
	if x[1]%height == 0 and x[1] != 0:
		pink = x[0]

