S_V = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, }
def solution(roman):
	print(roman)
	"""complete the solution by transforming the roman numeral into an integer"""
	roman = [S_V[x] for x in roman]
	for i in range(len(roman) - 1):
		if roman[i] < roman[i + 1]:
			roman[i], roman[i + 1] = 0,roman[i + 1] - roman[i]
	return sum(roman)




print(solution('MMMCDLXIV'))


# 汪小佬
def solution1(roman):
	"""complete the solution by transforming the roman numeral into an integer"""
	return sum([S_V[roman[i]] if S_V[roman[i]] >= S_V[roman[i + 1]] else -S_V[roman[i]] for i in range(len(roman) - 1)])\
	       + S_V[roman[-1]]

# 大佬鼠
from functools import reduce
def solution2(roman):
	d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
	return reduce(lambda x, y: x + y if x >= y else y - x, (d[c] for c in roman))