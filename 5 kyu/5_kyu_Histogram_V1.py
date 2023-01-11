def histogram(rolls):
	cur = [['#'] * x + [str(x)] + [' '] * (max(rolls) - x) if x else [' '] * (max(rolls) + 1) for x in rolls]
	res = []
	for j in range(max(rolls) + 1):
		res.append((''.join(cur[i][j] + ' ' * (len(cur[i][j]) % 2) for i in range(len(cur)))).rstrip())
	return '\n'.join(res[::-1]) + '\n' + '-' * 11 + '\n' + '1 2 3 4 5 6' + '\n'

roll = [14, 8, 14, 5, 8, 11]
print(histogram(roll))


# 大佬鼠
def histogram(rolls):
	hist = "-----------\n1 2 3 4 5 6\n"
	for i in range(max(rolls)+1):
		hist = ''.join(['# ' if i < v else '{:<2d}'.format(i) if i == v and v != 0 else '  ' for v in rolls]).rstrip() + '\n' + hist
	return hist
