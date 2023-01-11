def parse(data):
	count, res = 0, []
	for x in data:
		if x == 'i':
			count += 1
		if x == 'd':
			count -= 1
		if x == 's':
			count = count ** 2
		if x == 'o':
			res.append(count)
	return res


print(parse("isoisoiso"))

# 大佬鼠
def parse(data):
	v, r = 0, []
	for c in data:
		v, r = v + {'i': 1, 'd': -1, 's': v * (v - 1)}.get(c, 0), r + [v] * (c == 'o')
	return r