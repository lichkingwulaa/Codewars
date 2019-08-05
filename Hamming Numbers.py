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