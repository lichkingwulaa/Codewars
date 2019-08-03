def last_digit(n1, n2):
	if int(list(str(n2 % 4))[-1]) == 0 and n2 != 0:
		return int(list(str(n1 ** 4))[-1])
	else:
		return int(list(str(n1**(n2 % 4)))[-1])
	
a = last_digit(1606938044258990275541962092341162602522202993782792835301376,2037035976334486086268445688409378161051468393665936250636140449354381299763336706183397376)
print(a)

# 汪小佬的代码解析
def last_digit1(n1,n2):
	return int(list(str(n1 ** 4))[-1]) if int(list(str(n2 % 4))[-1]) == 0 and n2 != 0 else  int(list(str(n1**(n2 % 4)))[-1])

# 大佬鼠的迷惑方法
def last_digit2(n1, n2):
	return (n1 % 10) ** (n2 % 4 + 4 * bool(n2)) % 10