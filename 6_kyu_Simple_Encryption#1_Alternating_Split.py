def decrypt(encrypted_text, n):
	while n > 0:
		even = [encrypted_text[i] for i in range(len(encrypted_text) // 2)] + ['']
		others = [encrypted_text[i] for i in range(len(encrypted_text) // 2, len(encrypted_text))]
		encrypted_text = ''.join(others[i] + even[i] for i in range((len(encrypted_text) + 1) // 2))
		n -= 1
	return encrypted_text


def encrypt(text, n):
	while n > 0:
		even = ''.join(text[i] for i, x in enumerate(text) if i % 2)
		others = ''.join(text[i] for i, x in enumerate(text) if not i % 2)
		text = even + others
		n -= 1
	return text



print(encrypt("This is a test!", 2))
print(decrypt("hskt svr neetn!Ti aai eyitrsig", 1))


# 大佬鼠
def decrypt(text, n):
	if text in ("", None):
		return text
	
	ndx = len(text) // 2
	
	for i in range(n):
		a = text[:ndx]
		b = text[ndx:]
		text = "".join(b[i:i + 1] + a[i:i + 1] for i in range(ndx + 1))
	return text


def encrypt(text, n):
	for i in range(n):
		text = text[1::2] + text[::2]
	return text