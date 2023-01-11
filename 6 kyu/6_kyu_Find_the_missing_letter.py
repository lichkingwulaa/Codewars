def find_missing_letter(chars):
	return [x for x in [chr(i) for i in range(ord(chars[0]), ord(chars[-1]) + 1)] if x not in chars][0]

print(find_missing_letter(['a', 'b', 'c', 'd', 'f']))


# 大佬鼠
def find_missing_letter1(chars):
	n = 0
	while ord(chars[n]) == ord(chars[n+1]) - 1:
		n += 1
	return chr(1+ord(chars[n]))


def find_missing_letter2(c):
	return next(chr(ord(c[i])+1) for i in range(len(c)-1) if ord(c[i])+1 != ord(c[i+1]))