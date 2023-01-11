"""
https://www.codewars.com/kata/primorial-of-a-number/python
"""
def num_primorial(n):
	prime = [2,]
	num = 1
	for x in range(3, 8000, 2):
		for i in range(3, x // 3 + 1, 2):
			if x % i == 0: break
		else:
			prime.append(x)
	for i in range(n):
		num *= prime[i]
	return num


print(num_primorial(3),30)
print(num_primorial(4),210)
print(num_primorial(5),2310)
print(num_primorial(8),9699690)
print(num_primorial(9),223092870)
