def beeramid(bonus, price):
	n = int(bonus / price)
	for i in range(1, n + 2):
		if i * (i + 1) * (2 * i + 1) / 6 > n:
			return i -1
	return 0

print(beeramid(-10, 2))

# 汪小佬
def beeramid1(bonus, price):
	n = int(max(bonus, 0) / price)
	return next(i - 1 for i in range(1, n + 2) if i * (i + 1) * (2 * i + 1) / 6 > n)

print(beeramid(-10, 2))


# 大佬鼠(！！！！！)
from itertools import count
def beeramid2(bonus, price):
	n = int(max(bonus, 0) / price)
	return next(i - 1 for i in count(int((n*3)**(1/3)+1),-1) if i * (i + 1) * (2 * i + 1) / 6 > n)
