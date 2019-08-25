import time
x = time.time()

def F(n, a, b):
	while n >= 2:
		if n % 2:
			a, b = a, a+b
		else:
			a, b = a + b, b
		n //= 2
	return a + b if n else b


def fusc(n):
	print(n)
	if n <= 1:
		return n
	while (n % 2) == 0:
		n //= 2
	return F(n // 2, 1, 1)


print(fusc(0))
print(fusc(1))
print(fusc((1<<1000) + 1))
print(fusc((1<<1000) - 1))
print(fusc((1<<1000) + 5))
print(fusc((1<<1000) + 21))

y = time.time()
print(y - x)