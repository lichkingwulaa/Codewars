def hamming(n):
	"""Returns the nth hamming number"""
	k1, k2, k3 = 0, 0, 0
	res = [1]
	for i in range(1, n):
		s1 = res[k1] * 2
		s2 = res[k2] * 3
		s3 = res[k3] * 5
		min_val = min(s1, s2, s3)
		res.append(min_val)
		if res[i] == s1:
			k1 += 1
		if res[i] == s2:
			k2 += 1
		if res[i] == s3:
			k3 += 1
	return res[-1]

print(hamming(1))



# 大佬鼠的暴力解法
# (确定最大汉明数，直接生成汉明数列表)

h = sorted(2**i*3**j*5**k for i in range(35) for j in range(25) for k in range(15))

def hamming(n):
	return h[n-1]