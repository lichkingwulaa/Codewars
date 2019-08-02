# 有效的括号
def valid_parentheses(string):
	string = list(string)
	if len(string) == 0:
		return True
	i = 0
	while True:
		if string[i] != '(' and string[i] != ')':
			del string[i]
			i = 0
		else:
			i += 1
		for j in range(len(string)):
			if string[j] != '(' and string[j] != ')':
				break
		else:
			break
	i = 0
	while i<len(string)-1:
		if string[i] == '(' and string[i+1] == ')':
			del string[i]
			del string[i]
			i = 0
		else:
			i += 1

	return len(string) == 0


a = valid_parentheses('')
print(a)


# 大佬鼠的迷惑方法
def valid_parentheses(string):
	cnt = 0
	for char in string:
		if char == '(': cnt += 1
		if char == ')': cnt -= 1
		if cnt < 0: return False
	return True if cnt == 0 else False