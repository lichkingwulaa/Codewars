import itertools
def next_bigger(n):
	print(n)
	res = sorted(int(''.join(x)) for x in itertools.permutations(str(n), len(str(n))))
	return -1 if res.index(n) == len(res) - 1 else res[res.index(n) + 1]

print((next_bigger(9)))


# 汪小佬
from itertools import permutations
def next_bigger1(n):
	i = len(str(n)) - 1     # 确定变换数字的后几位，i
	while i > 0:
		if str(n)[i - 1] < str(n)[i]:
			break
		i -= 1
	res = sorted(set(''.join(x) for x in permutations(str(n)[i - 1:], len(str(n)[i - 1:]))))   # 后几位数字的全排列
	return int(str(n)[:i - 1] + res[res.index(str(n)[i - 1:]) + 1]) if i else -1


# 大佬鼠
def next_bigger2(n):
	s = list(str(n))
	for i in range(len(s)-2,-1,-1):
		if s[i] < s[i+1]:
			t = s[i:]
			m = min(filter(lambda x: x>t[0], t))
			t.remove(m)
			t.sort()
			s[i:] = [m] + t
			return int("".join(s))
	return -1