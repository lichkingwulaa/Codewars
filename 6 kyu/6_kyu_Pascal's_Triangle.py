def pascals_triangle(n):
	res = [ [1], ]
	for i in range(1, n):
		res.append([1] + [ res[i - 1][j] + res[i - 1][j + 1] for j in range(len(res[i - 1]) - 1) ] + [1])
	return [y for x in res for y in x]

pascals_triangle(4)


# 大佬鼠
def pascals_triangle1(n):
	if n == 1:
		return [1]
	prev = pascals_triangle(n - 1)
	return prev + [1 if i == 0 or i == n -1 else prev[-i] + prev[-(i + 1)] for i in range(n)]


from math import factorial
def comput_nk(n, k):
	return factorial(n) // (factorial(n - k) * factorial(k))
def pascals_triangle2(n):
	return [comput_nk(n, k) for n in range(n) for k in range(n + 1)]



from itertools import islice, chain

def p():
	xs = [1]
	while True:
		yield xs
		xs = [a + b for a, b in zip([0] + xs, xs + [0])]

def pascals_triangle3(n):
	return list(chain.from_iterable(islice(p(), n)))


from scipy.special import comb
def pascals_triangle(n):
	return [comb(a, b, exact=True) for a in range(n) for b in range(a + 1)]