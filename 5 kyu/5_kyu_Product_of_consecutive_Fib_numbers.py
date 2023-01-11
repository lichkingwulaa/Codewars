def productFib(prod):
	a, b = 0, 1
	while True:
		if a * b == prod:
			return [a, b, True]
		elif a * b > prod:
			return [a, b, False]
		else:
			a, b = b, a + b


print(productFib(4895), [55, 89, True])
print(productFib(5895), [89, 144, False])


# 大佬鼠
def productFib(prod):
	a, b = 0, 1
	while prod > a * b:
		a, b = b, a + b
	return [a, b, prod == a * b]