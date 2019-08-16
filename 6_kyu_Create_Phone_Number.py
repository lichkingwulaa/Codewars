def create_phone_number(n):
	n = ''.join(str(x) for x in n)
	return '({}) {}-{}'.format(n[0:3], n[3:6], n[7:])

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))


# 大佬鼠
def create_phone_number(n):
	return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
