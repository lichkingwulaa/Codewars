def digital_root(n):
	while True:
		n = sum(int(x) for x in str(n))
		if 0 <= n <= 9:
			return n

print(digital_root(942))


# 大佬鼠
def digital_root1(n):
	return n if n < 10 else digital_root(sum(map(int,str(n))))

def digital_root2(n):
	return n % 9 or n and 9     # (n % 9) or (n and 9)

def digital_root(n):
	return 1 + ((int(n) - 1) % 9) if n>0 else 0