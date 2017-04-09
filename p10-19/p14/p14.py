from PIL import Image, ImageDraw
import math

wire = Image.open("wire.png")
length = wire.width
coil = Image.new('RGB', (math.ceil(math.sqrt(length)), math.ceil(math.sqrt(length))), 0)
coilDraw = ImageDraw.Draw(coil)

#for every turn, go twice the same
x = math.ceil(math.sqrt(length)/2)
y = math.ceil(math.sqrt(length)/2)
#dir: 0=left; 1=down; 2=right; 3=up;
direction = 0
lastCount = 1
count = 1
iteration = 1
xy = (x,y)
coilDraw.point(xy, wire.getpixel((length-1,0)))


#function draws inside out
for i in range(2, length):
	if direction >= 4:
		direction = 0

	#change movement based on direction
	if direction == 0:
		x = x-1
	elif direction == 1:
		y = y+1
	elif direction == 2:
		x = x+1
	elif direction == 3:
		y = y-1

	count = count - 1

	#repeat for however many times necessary
	if count == 0:
		direction = direction+1
		iteration = iteration + 1
		count = lastCount
		if iteration == 3:
			lastCount = lastCount+1
			count = lastCount
			iteration = 1

	xy = (x, y)
	coilDraw.point(xy, wire.getpixel((length-i, 0)))

#drawn upside down
coil = coil.rotate(180)
coil.save("coil.png")