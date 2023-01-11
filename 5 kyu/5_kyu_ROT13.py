def rot13(message):
	res = ''
	for x in message:
		if x.isalpha():
			if ord('A') <= ord(x.upper()) < ord('N'):
				res += chr(ord(x) + 13)
			else:
				res += chr(ord(x) - 13)
		else:
			res += x
	return res

print(rot13("This is my first ROT13 excercise!"))

# 大佬鼠
def rot13a(message):
	return message.encode('rot13')


def rot13b(message):
	first = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
	trance = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
	return message.translate(str.maketrans(first, trance))