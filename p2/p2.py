def translate(str):
	temp = ""
	for c in str:
		if c >= 'a' and c <= 'x':
			c = chr(ord(c) + 2)
		elif c == 'y':
			c = 'a'
		elif c == 'z':
			c = 'b'

		temp += c

	return temp

print(translate("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."))

key = translate("map")
print("key is %s" % key)
print("http://www.pythonchallenge.com/pc/def/%s.html" % key)