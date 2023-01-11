"""
https://www.codewars.com/kata/find-the-divisors/solutions/python
"""
def divisors(integer):
	res = [i for i in range(2, integer // 2 + 1) if not integer % i]
	return res if res else str(integer) + " is prime"


print(divisors(15))#, [3, 5]);
print(divisors(12))#, [2, 3, 4, 6]);
print(divisors(13))#, "13 is prime");


# 大佬鼠 注意or的使用
def divisors(n):
	return sorted(i for i in range(2, n // 2 + 1) if not n % i) or '{} is prime'.format(n)