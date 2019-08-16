s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + 'abcdefghijklmnopqrstuvwxyz' + '0123456789' +  ".,:;-?! '()$%&" + '"'    # 77
def change(arr):
	return [x.upper() if i % 2 and x == x.lower() else x.lower() if i % 2 and x != x.lower() else x
	        for i, x in enumerate(arr)]

def decrypt(encrypted_text):
	if not encrypted_text:
		return encrypted_text
	encrypted_text = [s[-s.index(encrypted_text[0]) - 1]] + list(encrypted_text)[1:]
	res = [encrypted_text[0],]
	for i in range(1, len(encrypted_text)):
		num = s.index(res[i - 1]) - s.index(encrypted_text[i])
		res.append(s[(lambda a: a if a >= 0 else a + 77)(num)])
	res = change(res)
	return ''.join(res)

def encrypt(text):
	if not text:
		return text
	text = change(text)
	res = [s[-s.index(text[0]) - 1],]
	for i in range(1, len(text)):
		num = s.index(text[i - 1]) - s.index(text[i])
		res.append(s[(lambda a: a if a >= 0 else a + 77)(num)])
	return  ''.join(res)

print(encrypt("This is a test!"))