from math import log
# 返回多对值
def isPP(n):
	num = { '0': [10],              '1': [3, 7, 9, 11],     # 注意此处，1改为11,log(n,m)中m不可为0
			'2': [2, 8],            '3': [3, 7],            '4': [2, 4, 8],     '5': [5],
			'6': [2, 4, 6, 8],      '7': [3, 7],            '8': [2, 8],        '9': [3, 7, 9]  }
	pick_num = num[str(n)[-1]]
	result = []
	for m in pick_num:
		pick_num.append(m + 10)
		if round(log(n, m)) < 2:
			break
		if pow(m, round(log(n, m))) == n:
			result.append([m, round(log(n, m))])
			break
	if len(result) == 0:
		return None
	elif len(result) == 1:
		return result[0]
	else:
		return result


print(isPP(121))

# 返回一对值
from math import *
def isPP(n):
	for m in range(2, round(sqrt(n) + 2)):
		for k in range(2, round(log(n, m)) + 2):
			if m ** k == n:
				return [m, k]
	return None
"""
1 ->1 1 1 1
2 ->2 4 8 6
3 ->3 9 7 1
4 ->4 6
5 ->5
6 ->6
7 ->7 9 3 1
8 ->8 4 2 6
9 ->9 1
"""