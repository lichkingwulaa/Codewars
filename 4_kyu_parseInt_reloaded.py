d = {
	'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
	'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
	'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70,
	'eighty': 80, 'ninety': 90, 'hundred': 100, 'thousand': 1000, 'million': 1000000, 'and': 1, }
def parse_int(string):
	s = string.split(' ')
	r = []
	for x in s:
		if '-' in x:
			x = d[x.split('-')[0]] + d[x.split('-')[1]]
			r.append(x)
		else:
			r.append(d[x])
	curr, i, res = 1, 0, []
	while i < len(r):
		if r[i - 1] == 100 and r[i] == 1000 and i > 0:
			i += 1
			continue
		curr *= r[i]
		if (r[i] == 100 and 1000 not in r[i:]) or r[i] == 1000:
			res.append(curr)
			curr = 1
		elif r[i] == 100 and 1000 in r[i:]:
			res.append(curr * 1000)
			curr = 1
		i += 1
	if s[-1] in ['hundred', 'thousand']:
		curr = 0
	return sum(res) + curr


print(parse_int('seven hundred thousand'), 700000)
print(parse_int('twenty'), 20)
print(parse_int('two hundred forty-six'), 246)
print(parse_int("seven hundred eighty-three thousand nine hundred and nineteen"), 783919)


# 大佬鼠
words = {w: n for n, w in enumerate('zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split())}
words.update({w: 10 * n for n, w in enumerate('twenty thirty forty fifty sixty seventy eighty ninety hundred'.split(), 2)})
thousands = {w: 1000 ** n for n, w in enumerate('thousand million billion trillion quadrillion quintillion sextillion septillion octillion nonillion decillion'.split(), 1)}
def parse_int(strng):
	num = group = 0
	for w in strng.replace(' and ', ' ').replace('-', ' ').split():
		if w == 'hundred': group *= words[w]
		elif w in words: group += words[w]
		else:
			num += group * thousands[w]
			group = 0
	return num + group