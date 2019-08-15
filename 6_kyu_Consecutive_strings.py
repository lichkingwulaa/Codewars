def longest_consec(strarr, k):
	if len(strarr) == 0 or k > len(strarr) or k <= 0:
		return ""
	res = ''.join(strarr[:k])
	for i in range(len(strarr) - k + 1):
		if len(''.join(strarr[i:i + k])) > len(res):
			res = ''.join(strarr[i:i + k])
	return res

print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx",
                      "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"],2))


# 大佬鼠
def longest_consec(s, k):
	return max(["".join(s[i:i+k]) for i in range(len(s)-k+1)], key=len) if s and 0 < k <= len(s) else ""
