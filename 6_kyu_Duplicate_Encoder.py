def duplicate_encode(word):
	word = word.lower()
	for x in set(word):
		if word.count(x) > 1:
			word = word.replace(x, '1')
		else:
			word = word.replace(x, '0')
	return word.replace('0', '(').replace('1', ')')

print(duplicate_encode("Success"))


# 大佬鼠
def duplicate_encode(word):
	return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])