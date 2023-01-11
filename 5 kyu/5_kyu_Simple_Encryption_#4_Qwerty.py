pick = ['qwertyuiopqwertyuiopQWERTYUIOPQWERTYUIOP',
        'asdfghjklasdfghjklASDFGHJKLASDFGHJKL',
        'zxcvbnm,.zxcvbnm,.ZXCVBNM<>ZXCVBNM<>']

def encrypt(text, encryptKey):
	encryptKey = ('00' + str(encryptKey))[-3:]
	res = []
	for x in text:
		if x.isalpha() or x in [',', '.', '<', '>']:
			for i in range(3):
				if x in pick[i]:
					num = (pick[i].index(x) + int(encryptKey[i]))
					res.append(pick[i][num])
		else:
			res.append(x)
	res = ''.join(res)
	return res

def decrypt(text, encryptKey):
	encryptKey = ('00' + str(encryptKey))[-3:]
	res = []
	for x in text:
		if x.isalpha() or x in [',', '.', '<', '>']:
			for i in range(3):
				if x in pick[i]:
					num = (pick[i][::-1].index(x) + int(encryptKey[i]))
					res.append(pick[i][::-1][num])
		else:
			res.append(x)
	res = ''.join(res)
	return res

print(encrypt(">fdd", 134))


# 大佬鼠
encrypt = lambda s, k: code(s, k)
decrypt = lambda s, k: code(s, k, -1)
def code(text, key, m=1):
	keys, r = [int(e) * m for e in str(key).rjust(3, '0')], []
	for c in text:
		for i, a in enumerate(['qwertyuiop', 'asdfghjkl', 'zxcvbnm,.']):
			if c in a: c = a[(a.index(c) + keys[i]) % len(a)]
		for i, a in enumerate(['QWERTYUIOP', 'ASDFGHJKL', 'ZXCVBNM<>']):
			if c in a: c = a[(a.index(c) + keys[i]) % len(a)]
		r.append(c)
	return ''.join(r)