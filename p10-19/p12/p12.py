file = open('evil2.gfx', 'rb').read()
#print(file)

for x in range(0,5):
	open("%i.jpg" %(x+1), 'wb').write(file[x::5])

print("Images generated.")
print("key is disproportional.")