"""
https://www.codewars.com/kata/growth-of-a-population/solutions/python
"""
def nb_year(p0, percent, aug, p):
	i = 0
	while p0 < p:
		p0 = p0 + p0 * percent / 100 + aug
		i += 1
	return i

print(nb_year(1500000, 0.25, 1000, 2000000))


# 大佬鼠
def nb_year(p0, percent, aug, p, years = 0):
	if p0 < p:
		return nb_year(p0 + int(p0 * percent / 100) + aug, percent, aug, p, years + 1)
	return years