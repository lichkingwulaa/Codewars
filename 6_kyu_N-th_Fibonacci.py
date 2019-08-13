def nth_fib(n):
	res = [0, 1, ]
	res += ( res[i] + res[i + 1] for i in range(n) )
	return res[n - 1]

nth_fib(6)


# 大佬鼠(递归)
def nth_fib1(n):
	if n <= 2:
		return n - 1
	else:
		return nth_fib(n-1)+nth_fib(n-2)


def nth_fib2(n):
	a, b = (0, 1)
	for _ in range(n-1):
		a, b = b, a + b
	return a


from math import sqrt

def nth_fib3(n):
	n = n - 1
	Phi = (1 + sqrt(5)) / 2
	phi = (1 - sqrt(5)) / 2
	return int(((Phi ** n) - (phi ** n)) / sqrt(5))