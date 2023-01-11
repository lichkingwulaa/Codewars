def wave(str):
	res = []
	for i in range(len(str)):
		if str[i] != ' ':
			s = list(str)
			s[i] = chr(ord(str[i]) - 32)
			res.append(''.join(s))
	return res

print(wave('hey  you'))

# 汪小佬
def wave1(str):
	return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i] != ' ']

# 大佬鼠
def wave2(str):
	return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]