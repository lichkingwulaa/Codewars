"""
https://www.codewars.com/kata/reverse-or-rotate/python
"""
import re
def revrot(strng, sz):
	if sz <= 0 or not strng or sz > len(strng):
		return ''
	string = re.findall(r'.{'+str(sz)+'}', strng)
	res = []
	for x in string:
		num = sum(int(i) for i in x)
		if num % 2:
			res.append(x[1:] + x[0])
		else:
			res.append(x[::-1])
	return ''.join(res)

print(revrot("1234", 0), "")
print(revrot("", 0), "")
print(revrot("1234", 5), "")
s = "733049910872815764"
print(revrot(s, 5), "\n330479108928157")



import re
def revrot1(strng, sz):
	if sz <= 0 or not strng or sz > len(strng): return ''
	string = re.findall(r'.{'+str(sz)+'}', strng)
	return ''.join(x[1:] + x[0] if sum(int(i) for i in x) % 2 else x[::-1] for x in string)


def revrot2(strng, sz):
	func = lambda x : x[1:] + x[0] if sum(int(i) for i in x) % 2 else x[::-1]
	return "" if sz <= 0 or sz > len(strng) else "".join(func(strng[i:i+sz]) for i in range(0, len(strng) - sz + 1, sz))