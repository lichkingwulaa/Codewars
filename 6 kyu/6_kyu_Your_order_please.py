def order(sentence):
	if not sentence:
		return ''
	r = sorted( (sorted(x)[0], i)  for i, x in enumerate(sentence.split(' ')) )
	return ' '.join( sentence.split(' ')[ r[i][1] ]  for i in range(len(r)) )

print(order(""))


def order1(sentence):
	res = [''] * len(sentence.split(' '))
	num = [ y for x in sentence.split(' ') for y in x if '0' <= y <= '9' ]
	for i, j in enumerate(num):
		res[int(j) - 1] = sentence.split(' ')[i]
	return ' '.join(res)


# 大佬鼠
def order(words):
	return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))