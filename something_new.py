def find_uniq(arr):
	res = sorted((sorted(''.join(set(x.lower()))), x) for x in set(arr))
	return res[-1][1] if res[0][0] == res[1][0] else res[0][1]
print(find_uniq(['    ', '  ', ' ', 'a', ' ', '']))