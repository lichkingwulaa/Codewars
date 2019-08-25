def solution(args):
	num = [ x - i for i, x in enumerate(args)]
	pick_num = sorted(num.index(x) for x in set(num))
	res = []
	for i in range(len(pick_num) - 1):
		res.append(args[pick_num[i]: pick_num[i + 1]])
	return ','.join(str(x[0]) if len(x) == 1 else str(x[0]) + ',' + str(x[1]) if len(x) == 2  else str(x[0]) + '-' + str(x[-1])
	                for x in res + [args[pick_num[-1]:]])

print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]),
      '\n-6,-3-1,3-5,7-11,14,15,17-20')
print(solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]),
      '\n-3--1,2,10,15,16,18-20')