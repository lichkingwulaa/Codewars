def find_uniq(arr):
	res = []
	for x in arr:
		y = (''.join(set(x.lower())), x)
		res.append(y)
	res = sorted(res)
	if res[0][0] == res[1][0]:
		print(res[-1][1])
	else:
		print(res[0][1])
	
	
	res = sorted((''.join(set(x.lower())), x) for x in arr)
	return res[-1][1] if res[0][0] == res[1][0] else res[0][1]


print(find_uniq(['    ', '  ', ' ', 'a', ' ', '']))